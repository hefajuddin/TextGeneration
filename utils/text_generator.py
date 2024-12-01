def generate_text(prompt, model, max_length=100, temperature=0.7, top_k=50):
    """Generate text based on a given prompt."""
    return model(
        prompt,
        max_length=max_length,
        temperature=temperature,
        top_k=top_k,
        do_sample=True
    )