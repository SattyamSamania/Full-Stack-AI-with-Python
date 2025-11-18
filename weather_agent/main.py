from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
print("API Key loaded:", os.getenv("OPENAI_API_KEY"))
# Debug: Check if key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Did you create a .env file with OPENAI_API_KEY=...?")

# Initialize client
client = OpenAI(api_key=api_key)

def main():
    user_query = input("> ")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user_query}
        ]
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
