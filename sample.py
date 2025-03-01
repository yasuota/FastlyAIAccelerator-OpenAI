from openai import OpenAI
import os

client = OpenAI(
    # Set the API endpoint
    base_url="https://ai.fastly.app/api.openai.com/v1",
    # Set default headers
    default_headers={
        "Fastly-Key": os.getenv("FASTLYTOKEN_AI"),
        "api_Key": os.getenv("OPENAI_API_KEY")
    }

)
user_input = input("Enter your message: ")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": user_input
        }
    ]
)

print("ID: ", completion.id)
print("Answer: ", completion.choices[0].message.content)
