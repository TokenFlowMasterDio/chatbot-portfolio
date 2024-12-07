const BACKEND_URL = "https://diochatbot.herokuapp.com"; // Replace with your Heroku app URL

document.getElementById("sendButton").addEventListener("click", async function () {
    const userMessage = document.getElementById("userMessage").value;

    try {
        const response = await fetch(`${BACKEND_URL}/chat`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: userMessage })
        });

        if (response.ok) {
            const data = await response.json();
            document.getElementById("response").innerText = data.reply;
        } else {
            document.getElementById("response").innerText = "Error: Unable to get a response from the server.";
        }
    } catch (error) {
        document.getElementById("response").innerText = `Error: ${error.message}`;
    }
});
