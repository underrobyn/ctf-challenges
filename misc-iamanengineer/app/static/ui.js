function messageTimeAgo() {
    // Get all elements with the data-message-time attribute
    let elements = document.querySelectorAll('[data-message-time]');
    // Iterate over each element
    elements.forEach(function (element) {
        let timestamp = element.getAttribute('data-message-time');
        let date = new Date(timestamp);

        // Calculate the minutes/hours since the timestamp
        let diff = Math.round((new Date() - date) / 1000 / 60);
        let text = diff + (diff === 1 ? ' min ago' : ' mins ago');
        if (diff > 59) {
            diff = Math.round((new Date() - date) / 1000 / 60 / 60);
            text = diff + (diff === 1 ? ' hour ago' : ' hours ago');
        }

        // Update the content of the element
        element.textContent = text;

        // Update the content every minute/hour
        setInterval(function () {
            let diff = Math.round((new Date() - date) / 1000 / 60);
            let text = diff + (diff === 1 ? ' min ago' : ' mins ago');
            if (diff > 59) {
                diff = Math.round((new Date() - date) / 1000 / 60 / 60);
                text = diff + (diff === 1 ? ' hour ago' : ' hours ago');
            }
            element.textContent = text;
        }, 60000);
    });
}

function countEmails() {
    let ic = document.getElementById('inbox_count');
    let emails = document.querySelectorAll('#email_list a');
    ic.innerText = emails.length;
    document.title = `InLook | Inbox (${emails.length})`;
}

document.addEventListener('DOMContentLoaded', function () {
    messageTimeAgo();
    countEmails();
});
