from transformers import AutoModelForCausalLM, AutoTokenizer

# Load Llama model and tokenizer
model_name = "meta-llama/Llama-3.2-1B"  # Adjust to your exact model path/name
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

print("Llama model loaded successfully!")
