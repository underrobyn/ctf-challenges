import logging
from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask, abort, session, request, jsonify, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from os import environ
from .utils import update_conversation, clean_history, calculate_weight, TOKEN_USAGE_LIMIT, CONVERSATION_MESSAGE_LIMIT,\
    INITIAL_MESSAGE, EMAIL_LIST, out_error, get_user_message_count


app = Flask(__name__, static_folder='static', template_folder='templates')

app.config['RATELIMIT_HEADERS_ENABLED'] = True
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_KEY_PREFIX'] = 'rctf_misc_jeffrey_'
app.config['SECRET_KEY'] = environ['APP_SECRET_KEY']

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["50 per minute", "500 per hour"],
    storage_uri="memory://",
)


@app.template_filter('custom_date_format')
def custom_date_format(offset_in_mins: int):
    current_time = datetime.now()
    offset = timedelta(minutes=int(offset_in_mins))
    new_time = current_time - offset
    formatted_time = new_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time


@app.errorhandler(429)
def handle_rate_limit_exceeded(e):
    return jsonify(out_error(f'{e}')), 429


@app.after_request
def apply_headers(response):
    response.headers["Server"] = "EmailClient/1.0"

    if request.path.startswith('/api/'):
        response.headers['Access-Control-Allow-Origin'] = '*'

    return response


@app.route('/api/ping', methods=['GET'])
@limiter.limit("1 per second")
def api_ping():
    return jsonify({
        'error': False,
        'response': 'pong'
    })


@app.route('/api/response', methods=['POST'])
@limiter.limit("5 per minute")
def api_response():
    data = request.get_json()
    user_message = data.get('message')
    email_id = data.get('email_id')
    if email_id not in EMAIL_LIST:
        return abort(404)

    ai_response = update_conversation(email_id, user_message, session)

    return jsonify(ai_response)


@app.route('/api/clear/<email_id>', methods=['GET'])
def api_clear(email_id: str):
    if email_id not in EMAIL_LIST:
        return abort(404)

    session[f'conversation_{email_id}'] = []

    return jsonify({
        'error': False,
        'response': f'Cleared history for {email_id}'
    })


@app.route('/api/history', methods=['POST'])
@limiter.limit("10 per minute")
def api_history():
    data = request.get_json()
    email_id = data.get('email_id')
    if email_id not in EMAIL_LIST:
        return abort(404)

    history = session.get(f"conversation_{email_id}", [])
    safe_history = clean_history(history)
    user_message_count = get_user_message_count(history)

    token_use_count = 0
    if len(history) == 0:
        safe_history.append({
            'role': 'assistant',
            'content': INITIAL_MESSAGE[email_id]
        })
    else:
        token_use_count = calculate_weight(history)

    return jsonify({
        'error': False,
        'response': safe_history,
        'message_limit': CONVERSATION_MESSAGE_LIMIT,
        'message_count': user_message_count,
        'tokens': token_use_count,
        'token_limit': TOKEN_USAGE_LIMIT
    })


@app.route('/email/<email_id>', methods=['GET'])
def email_client(email_id: str):
    if email_id not in EMAIL_LIST:
        return abort(404)

    return render_template('email.html',
                           email_id=email_id,
                           name=EMAIL_LIST[email_id],
                           default_msg=INITIAL_MESSAGE[email_id],
                           token_max=TOKEN_USAGE_LIMIT)


def main():
    load_dotenv()
    logging.basicConfig(level=logging.WARNING, format='%(levelname)s:%(asctime)s - %(message)s')

    for env_var in ['APP_SECRET_KEY', 'OPENAI_API_KEY']:
        if env_var not in environ:
            logging.error(f'{env_var} is not defined in the environment')
            exit(1)

    app.run(debug=False, port=5000)


if __name__ == '__main__':
    main()
