import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)
CORS(app)

# Load Hugging Face model
model_name = "gpt2"  # Replace with your model name
api_key = os.getenv("HUGGINGFACE_API_KEY")  # Get API key from environment variable

if not api_key:
    raise ValueError("Hugging Face API key not found. Ensure HUGGINGFACE_API_KEY is set in the environment.")

model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=api_key)
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=api_key)

@app.route("/")
def home():
    return "Chatbot server is running. Use the frontend to interact."

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message", "")
        if not user_input:
            return jsonify({"error": "No input message provided"}), 400

        inputs = tokenizer.encode(user_input, return_tensors="pt")
        outputs = model.generate(inputs, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use the PORT from the environment variable
    app.run(host="0.0.0.0", port=port)
