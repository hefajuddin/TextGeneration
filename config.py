CONFIG = {
    "model_name": "gpt2",  # Pre-trained GPT-2 model from Hugging Face
    "max_length": 100,     # Maximum length of generated text
    "temperature": 0.7,    # Controls randomness (lower = more deterministic)
    "top_k": 50,           # Use top-k sampling for text generation
    "device": "cuda"       # Use GPU if available
}