const EMAIL_ID = document.body.getAttribute('data-emailid');
let waiting = false;

function setupEventListeners() {
    const userInput = document.getElementById("user-input");
    const userSubmit = document.getElementById("send-chat");

    userInput.addEventListener("keydown", (event) => {
        if (event.key !== "Enter") return;
        if (waiting) return;
        const message = userInput.value.trim();
        if (message !== "") sendMessage(message);
        userInput.value = "";
    });
    userSubmit.addEventListener("click", (event) => {
        const message = userInput.value.trim();
        if (waiting) return;
        if (message !== "") sendMessage(message);
        userInput.value = "";
    });
}

function updateMessageBox(data) {
    const chatBox = document.getElementById("chat-box");
    const tokenText = document.getElementById("token-use");

    chatBox.innerHTML = '';

    let message_map = {
        'system': 'system-message',
        'user': 'user-message',
        'assistant': 'assistant-message'
    };

    if (data.error) {
        const serverResponseEl = document.createElement("div");
        serverResponseEl.classList.add("message", "system-message");
        serverResponseEl.innerText = data.response;
        chatBox.appendChild(serverResponseEl);
    } else {
        for (let message in data.response) {
            let chatEl = document.createElement("div");
            chatEl.classList.add("message", message_map[data.response[message]['role']]);
            chatEl.innerText = data.response[message]['content'];
            chatBox.appendChild(chatEl);
        }

        tokenText.innerText = `Token usage for this chat: ${data.tokens}/${data.token_limit}`
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}

function conversationResume() {
    fetch("/api/history", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            'email_id': EMAIL_ID
        }),
    })
        .then((response) => response.json())
        .then(updateMessageBox)
        .catch((error) => {
            console.error("Error:", error);
        });
}

function sendMessage(message) {
    waiting = true;

    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");
    const userSubmit = document.getElementById("send-chat");
    const userMessageElement = document.createElement("div");

    userInput.disabled = true;
    userSubmit.disabled = true;
    userMessageElement.classList.add("message", "user-message-loading");
    userMessageElement.innerText = message;
    chatBox.appendChild(userMessageElement);

    fetch("/api/response", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            'message': message,
            'email_id': EMAIL_ID
        }),
    })
    .then((response) => response.json())
    .then(updateMessageBox)
    .catch((error) => {
        console.error("Error:", error);
    }).finally(() => {
        userInput.disabled = false;
        userSubmit.disabled = false;
        waiting = false;
    });
}

document.addEventListener("DOMContentLoaded", () => {
    //setupEventListeners();
    // conversationResume();
});
