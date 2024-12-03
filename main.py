from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

app = Flask(__name__)
CORS(app)

# Load environment variables
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
if not HUGGINGFACE_API_KEY:
    raise ValueError("Hugging Face API key not found. Ensure HUGGINGFACE_API_KEY is set in the environment.")

# Load model and tokenizer
model_name = "meta-llama/Llama-3.2-1B"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=HUGGINGFACE_API_KEY)
model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=HUGGINGFACE_API_KEY)

# Default route
@app.route("/")
def home():
    return "Chatbot server is running. Use the frontend to interact."

# Chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    """
    Handle chat requests.
    Expects a JSON payload with a 'message' key.
    """
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Tokenize and generate response
    inputs = tokenizer(user_message, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)
    bot_message = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({"response": bot_message})

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
