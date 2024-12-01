from config import CONFIG
from utils.data_loader import load_prompts
from models.llm_model import get_text_generation_model
from utils.text_generator import generate_text

def main():
    # Load the model
    model = get_text_generation_model(CONFIG["model_name"], CONFIG["device"])

    # Load prompts
    prompts = load_prompts("data/prompts.json")

    # Generate text for each prompt
    for prompt_data in prompts:
        prompt = prompt_data["prompt"]
        print(f"\nPrompt: {prompt}\n")
        
        # Generate text
        outputs = generate_text(
            prompt,
            model,
            max_length=CONFIG["max_length"],
            temperature=CONFIG["temperature"],
            top_k=CONFIG["top_k"]
        )
        
        for i, output in enumerate(outputs):
            print(f"Generated Text {i + 1}: {output['generated_text']}\n")

if __name__ == "__main__":
    main()
