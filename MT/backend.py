import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# Load .env variable
load_dotenv()

# Hugging Face API key
HF_KEY = os.getenv("HF_KEY")
if not HF_KEY:
    raise ValueError("HF_KEY is not set")

# Initializing the InferenceClient
client = InferenceClient(token=HF_KEY)

def query_deepseek(prompt):
    if not prompt:
        return "No prompt provided."

    try:
        response = client.text_generation(
            prompt=prompt,
            model="mistralai/Mistral-7B-Instruct-v0.1",
            max_new_tokens=500, 
            temperature=0.7,  
            return_full_text=False 
        )

        return response

    except Exception as e:
        # Logging the error
        print(f"Error occurred: {e}")
        return "An error occurred while processing your request. Please try again later."