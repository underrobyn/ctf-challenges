import os
import openai
import tiktoken
from os.path import isfile
from time import time, sleep
from PromptFileParser import PromptError, PromptParser


MODEL = "gpt-3.5-turbo"
TOKEN_USAGE_LIMIT = 850
CONVERSATION_MESSAGE_LIMIT = 7
enc = tiktoken.encoding_for_model(MODEL)


EMAIL_LIST = {
    "social": "jeffrey.jones@clam-corp.com"
}

INITIAL_MESSAGE = {
    "social": "Send an email to Jeffrey begin."
}


def read_prompt(email_id: str) -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    prompt_path = f'{dir_path}/prompts/{email_id}.prompt'

    if not isfile(prompt_path):
        raise PromptError(f'Prompt not found')

    pf = PromptParser(prompt_path)

    if pf.model != MODEL:
        raise PromptError(f'Prompt model of {pf.model} does not match system required model')

    return pf.get_prompt()


def out_error(msg) -> dict:
    return {
        "time": time(),
        "error": True,
        "response": str(msg)
    }


def calculate_weight(conversation: dict) -> int:
    token_total = 0

    for message in conversation:
        msg_count = len(enc.encode(message['content']))
        token_total += msg_count
        print(msg_count, message['content'])

    return token_total


def clean_history(conversation_history: dict) -> list:
    user_conversation = []
    for message in conversation_history:
        if message['role'] != 'system':
            user_conversation.append(message)

    return user_conversation


def get_user_message_count(conversation_history: dict) -> int:
    return sum(1 for message in conversation_history if message['role'] == 'user')


def update_conversation(email_id, user_message, session) -> dict:
    session_key = f"conversation_{email_id}"
    conversation_history = session.get(session_key, [])

    if not conversation_history:
        try:
            conversation_history.append({
                "role": "system",
                "content": read_prompt(email_id)
            })
        except PromptError as err:
            return out_error(err)

        conversation_history.append({
            "role": "assistant",
            "content": INITIAL_MESSAGE[email_id]
        })

    conversation_history.append({"role": "user", "content": user_message})
    current_conversation_weight = calculate_weight(conversation_history)
    user_message_count = get_user_message_count(conversation_history)

    if current_conversation_weight > TOKEN_USAGE_LIMIT:
        history_tmp = clean_history(conversation_history)
        history_tmp.append({
            'role': 'system',
            'content': 'Token limit for chat has been reached'
        })
        return {
            "error": False,
            "response": history_tmp,
            "message_limit": CONVERSATION_MESSAGE_LIMIT,
            "message_count": user_message_count,
            "tokens": current_conversation_weight,
            "token_limit": TOKEN_USAGE_LIMIT
        }

    if user_message_count > CONVERSATION_MESSAGE_LIMIT:
        history_tmp = clean_history(conversation_history)
        history_tmp.append({
            'role': 'system',
            'content': 'Email conversation message limit reached and security team got involved.'
        })
        return {
            "error": False,
            "response": history_tmp,
            "message_limit": CONVERSATION_MESSAGE_LIMIT,
            "message_count": user_message_count,
            "tokens": current_conversation_weight,
            "token_limit": TOKEN_USAGE_LIMIT
        }

    try:
        openai_result = openai.ChatCompletion.create(
            model=MODEL,
            messages=conversation_history,
        )
        pass
    except openai.error.RateLimitError:
        return out_error("API experienced a rate limit error, please try again shortly")
    except Exception as err:
        return out_error(err)

    print(openai_result)

    output_choice = openai_result.choices[0]
    assistant_message = output_choice.message.content

    conversation_history.append({"role": "assistant", "content": assistant_message})

    session[session_key] = conversation_history

    return {
        "time": openai_result['created'],
        "error": False,
        "response": clean_history(conversation_history),
        "message_limit": CONVERSATION_MESSAGE_LIMIT,
        "message_count": user_message_count,
        "tokens": calculate_weight(conversation_history),
        "openai_tokens": openai_result['usage'],
        "token_limit": TOKEN_USAGE_LIMIT
    }
