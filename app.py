from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)

# Enable CORS
CORS(app)

# Load model and tokenizer
model_name = "meta-llama/Llama-3.2-1B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def clean_response(response):
    """
    Post-process the response to remove redundancy and improve readability.
    """
    sentences = response.split(". ")
    unique_sentences = list(dict.fromkeys(sentences))  # Remove duplicate sentences while maintaining order
    return ". ".join(unique_sentences)

@app.route("/chat", methods=["POST"])
def chat():
    # Get the message from the request
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Few-shot prompting: Guide the model with examples
    prompt = f"""
    You are a helpful assistant. Respond to the user's question clearly and concisely.

    Q: Who are you?
    A: I am a chatbot designed to assist you with your queries.

    Q: How can I reset my password?
    A: To reset your password, click on the "Forgot Password" link on the login page and follow the instructions.

    Q: What are your working hours?
    A: We are available 24/7 to assist you.

    Q: {user_input}
    A:"""

    # Generate the response with controlled parameters
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=150,          # Limit response length
        temperature=0.7,         # Balance randomness
        top_p=0.9,               # Nucleus sampling
        repetition_penalty=1.2   # Penalize repetitive phrases
    )

    raw_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    clean_res = clean_response(raw_response)

    # Limit the scope: Respond gracefully to out-of-scope queries
    if "I don't know" in clean_res or clean_res.strip() == "":
        clean_res = "I'm here to assist with customer service queries. Could you clarify your question?"

    return jsonify({"response": clean_res})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
