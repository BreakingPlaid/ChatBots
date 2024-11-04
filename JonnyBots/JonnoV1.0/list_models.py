import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    # Test if gpt-4-turbo is accessible
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "user", "content": "Hello, can you confirm model access?"}
        ]
    )
    print("gpt-4-turbo is accessible.")
except Exception as e:
    print("Error accessing gpt-4-turbo:", e)