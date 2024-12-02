from transformers import pipeline
import torch

def get_text_generation_model(model_name, device="cpu"):
    """Load a pre-trained text generation model."""
    if device == "cuda" and not torch.cuda.is_available():
        print("Warning: CUDA device specified, but no GPU is available. Falling back to CPU.")
        device = "cpu"
    return pipeline("text-generation", model=model_name, device=0 if device == "cuda" else -1)
