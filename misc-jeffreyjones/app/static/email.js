const EMAIL_ID = document.body.getAttribute('data-emailid');
let waiting = false;

function setupEventListeners() {
    const userInput = document.getElementById("user_email");
    const userSubmit = document.getElementById("send_email");

    userSubmit.addEventListener("click", (event) => {
        const message = userInput.value.trim();
        if (waiting) return;
        if (message !== "") sendMessage(message);
        userInput.value = "";
    });
}

function updateMessageBox(data) {
    const chatBox = document.getElementById("conversation_history");
    const tokenText = document.getElementById("challenge-limit");
    const lastEmailTitle = document.getElementById("latest_email_title");
    const lastEmailText = document.getElementById("latest_email_text");

    chatBox.innerHTML = '';

    let message_map = {
        'system': 'system-message',
        'user': 'user-message',
        'assistant': 'assistant-message'
    };

    let sender_map = {
        'system': 'Clam-Corp Mail Server &lt;postmaster@clam-corp.com&gt;',
        'user': 'You &lt;it-support@rctf-technical.wales&gt;',
        'assistant': 'Jeffrey Jones &lt;jeffrey.jones@clam-corp.com&gt;'
    };

    if (data.error) {
        const serverResponseEl = document.createElement("div");
        serverResponseEl.classList.add("message", "system-message");
        serverResponseEl.innerText = data.response;
        chatBox.appendChild(serverResponseEl);
    } else {
        let i = 0;
        let lastContent = '...';
        for (let message in data.response) {
            let chatEl = document.createElement("div");
            let from = sender_map[data.response[message]['role']]
            if (data.response[message]['content'] === 'Send an email to Jeffrey begin.') {
                from = sender_map['system'];
            }

            if (data.response.length > 1 && data.response[message]['content'] === 'Send an email to Jeffrey begin.') {
                continue;
            }

            chatEl.classList.add("card", "mb-2", message_map[data.response[message]['role']]);
            chatEl.innerHTML = `
                <div class="card-header">
                    <h5 class="card-title mb-0">${'Re: '.repeat(i)}Quick Question</h5>
                    <small>From: ${from}</small>
                </div>
                <div class="card-body">
                    <p class="card-text">${data.response[message]['content']}</p>
                </div>`
            lastContent = data.response[message]['content'];
            chatBox.prepend(chatEl);
            i++;
        }

        lastEmailTitle.innerText = `${'Re: '.repeat(i)}Quick Question`;
        lastEmailText.innerText = `${lastContent.substring(0, 16)}...`;
        tokenText.innerText = `Message count for this chat: ${data.message_count}/${data.message_limit}`
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

    const chatBox = document.getElementById("conversation_history");
    const userInput = document.getElementById("user_email");
    const userSubmit = document.getElementById("send_email");
    const userMessageElement = document.createElement("div");

    userInput.disabled = true;
    userSubmit.disabled = true;

    userMessageElement.classList.add("card", "mb-2", "border-info");
    userMessageElement.innerHTML = `
        <div class="card-header">
            <h5 class="card-title mb-0">Sending...</h5>
        </div>
        <div class="card-body">
            <p class="card-text">${message}</p>
        </div>`
    chatBox.prepend(userMessageElement);

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
    setupEventListeners();
    conversationResume();
});
