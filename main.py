import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load a conversational model
model_name = "microsoft/DialoGPT-medium"  # Medium model for better customer interaction
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Define FAQ and response templates for customer service
faq_responses = {
    "What are your hours?": "We are open Monday to Friday, 9 AM to 6 PM.",
    "How can I contact support?": "You can contact support at support@example.com or call us at 1-800-123-4567.",
    "Where are you located?": "Our headquarters are in New York City, but we operate globally.",
    "What services do you offer?": "We offer a range of services including product support, billing assistance, and technical troubleshooting."
}

# Define the chatbot response function
def chatbot_response(user_input):
    # Check for exact matches in FAQ
    for question, answer in faq_responses.items():
        if user_input.lower() in question.lower():
            return answer

    # Generate a fallback response using the model
    inputs = tokenizer.encode(user_input, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=150,
        num_return_sequences=1,
        temperature=0.6,  # Controlled randomness
        top_p=0.85,      # Diverse but relevant responses
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Gradio Interface
interface = gr.Interface(
    fn=chatbot_response,
    inputs="text",
    outputs="text",
    title="Customer Service Chatbot",
    description="Ask any questions about our services or support. The chatbot will assist you!"
)

# Launch Gradio Interface
if __name__ == "__main__":
    interface.launch(server_name="0.0.0.0", server_port=7860)
