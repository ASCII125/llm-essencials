import { marked } from "https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js";

const form = document.getElementById('chat-form');
const messages = document.getElementById('messages');
const required_label = document.getElementById('required-label');
const send_button = document.getElementById('send-button');


send_button.addEventListener('click', () => {
    send_button.disable = true;
    send_button.innerHTML = 'Sending...';
    send_button.style.cursor = 'default';
    send_button.style.opacity = '0.5';
})

function restoreButton() {
    send_button.disable = false;
    send_button.innerHTML = 'Send';
    send_button.style.cursor = 'pointer';
    send_button.style.opacity = '1';
}


form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const message = form.elements.message.value;

    if (!message) {
        required_label.style.display = 'block';
        restoreButton();
        return;
    }

    if (required_label.style.display === 'block') {
        required_label.style.display = 'none';
    }

    const response = await fetch('http://localhost:8000/llm/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'message': message })
    });
    const data = await response.json();

    messages.innerHTML += `
    <div class="rc-message">
        ${marked.parse(data.content)}
    </div>
    `;

    form.reset();
    restoreButton();
});