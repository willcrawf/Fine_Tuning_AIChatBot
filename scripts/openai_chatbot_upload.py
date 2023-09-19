import os
import openai
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve your API key from the environment variables
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Upload your dataset in JSONL format
response = openai.File.create(
    file=open("tshirt_inquiries_dataset.jsonl", "rb"),
    purpose='fine-tune'
)
print(response)

# Access specific attributes of the response
file_id = response['id']
status = response['status']

# Print specific attributes
print("File ID:", file_id)
print("Status:", status)
# Define the model you want to fine-tune from (e.g., "gpt-3.5-turbo")
# model = "gpt-3.5-turbo"

# # Create a fine-tuning job
# fine_tuning_job = openai.FineTuningJob.create(training_file="tshirt_inquiries_dataset", model="gpt-3.5-turbo")

# # Print the response to see details about the fine-tuning job
# print(fine_tuning_job)
