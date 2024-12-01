import json

def load_prompts(file_path):
    """Load prompts from a JSON file."""
    with open(file_path, "r") as f:
        data = json.load(f)
    return data