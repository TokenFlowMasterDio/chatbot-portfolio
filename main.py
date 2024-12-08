import os
from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

# Define a simple route for testing
@app.route("/")
def home():
    return "Chatbot is successfully running on Hugging Face Spaces!"

# Define another route for an API endpoint (example)
@app.route("/api/message", methods=["POST"])
def chatbot_response():
    return jsonify({"response": "This is a placeholder response from your chatbot."})

# Run the app using the PORT environment variable for deployment
if __name__ == "__main__":
    # Use PORT provided by the environment, default to 7860 if not found
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port)
