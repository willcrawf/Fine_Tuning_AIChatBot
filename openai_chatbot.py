import os
import openai
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve your API key from the environment variables
api_key = os.environ.get("OPENAI_API_KEY")

# Upload your dataset in JSONL format
openai.File.create(
    file=open("your_dataset.jsonl", "rb"),
    purpose='fine-tune'
)