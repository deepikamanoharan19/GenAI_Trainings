from openai import AzureOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

# Configuration
api_version = os.getenv("API_VERSION")
endpoint = os.getenv("ENDPOINT")
subscription_key =os.getenv("SUBSCRIPTION_KEY")
deployment = os.getenv("DEPLOYMENT")

# Create client
client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

# Create chat completion
response = client.chat.completions.create(
    model=deployment,
    messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "I am going to Paris, what should I see?"}
    ],
    max_tokens=1310,          # limit output tokens (adjust as needed)
    temperature=1.0,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

# Print response
print(response.choices[0].message.content)
