from transformers import pipeline

def get_text_generation_model(model_name, device="cpu"):
    """Load a pre-trained text generation model."""
    return pipeline("text-generation", model=model_name, device=0 if device == "cuda" else -1)