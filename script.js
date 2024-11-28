async function sendMessage() {
    const userInput = document.getElementById("user-input").value;

    const response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userInput }),
    });

    const data = await response.json();
    document.getElementById("response").innerText = data.response;
}
