// Replace this URL with your actual Render backend URL
const BACKEND_URL = "https://1a47f93c-5dd8-47dd-9d8d-9a8361e5e50e-00-3uhyx3dlqo2z3.worf.replit.dev";



// Function to send the user's message to the backend and display the response
async function sendMessage() {
    const userMessage = document.getElementById("user-input").value;

    if (!userMessage.trim()) {
        alert("Please enter a message.");
        return;
    }

    // Display the user's message in the chat
    appendMessage("User", userMessage);

    // Clear the input field
    document.getElementById("user-input").value = "";

    try {
        // Send the message to the backend
        const response = await fetch(`${BACKEND_URL}/chat`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message: userMessage }),
        });

        if (!response.ok) {
            throw new Error("Failed to fetch response from the backend.");
        }

        const data = await response.json();
        appendMessage("Chatbot", data.response);
    } catch (error) {
        console.error("Error:", error);
        appendMessage("Chatbot", "Sorry, there was an error. Please try again.");
    }
}

// Function to append a message to the chat
function appendMessage(sender, message) {
    const chatContainer = document.getElementById("chat-container");
    const messageElement = document.createElement("div");
    messageElement.classList.add("message", sender.toLowerCase());
    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatContainer.appendChild(messageElement);

    // Scroll to the latest message
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Add an event listener to the "Send" button
document.getElementById("send-button").addEventListener("click", sendMessage);

// Allow pressing "Enter" to send the message
document.getElementById("user-input").addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});
