import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama3-70b-8192"

def groq_chat(prompt, model=GROQ_MODEL, temperature=0.2, max_tokens=700):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=data, timeout=45)
    if response.status_code != 200:
        raise RuntimeError(f"Groq API Error: {response.text}")
    return response.json()["choices"][0]["message"]["content"]
