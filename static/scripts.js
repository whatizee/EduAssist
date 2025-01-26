function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    if (!userInput.trim()) return;

    const chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;

    fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ question: userInput }),
    })
    .then((response) => response.json())
    .then((data) => {
        chatbox.innerHTML += `<p><strong>Chatbot:</strong> ${data.response}</p>`;
        document.getElementById("userInput").value = "";
        chatbox.scrollTop = chatbox.scrollHeight;
    })
    .catch((error) => {
        chatbox.innerHTML += `<p><strong>Error:</strong> Could not get a response.</p>`;
    });
}
