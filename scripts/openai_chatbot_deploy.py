import os
import openai
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve your API key from the environment variables
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Define the model you want to fine-tune from (e.g., "gpt-3.5-turbo")
model = "gpt-3.5-turbo"

# Create a fine-tuning job using the file_id
fine_tuning_job = openai.FineTuningJob.create(training_file="file-Erf3zOleu38QfeSfIdRCHUv0", model="gpt-3.5-turbo")


# Print the response to see details about the fine-tuning job
print(fine_tuning_job)
