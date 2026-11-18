import os
import httpx
from dotenv import load_dotenv

load_dotenv(override=True)

response = httpx.post(
    "https://api.mistral.ai/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {os.getenv('MISTRAL_API_KEY')}"
    },
    json={
        "model": "ministral-14b-2512",
        "messages": [
            {"role": "user", "content": "Hello"}
        ],
        "max_tokens": 20
    },
    timeout=30
)

print("Status Code:", response.status_code)
print("Response:", response.text)
print("Retry After:", response.headers.get("retry-after"))


