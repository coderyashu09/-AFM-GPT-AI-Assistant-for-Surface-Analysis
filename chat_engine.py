import requests
import json

def ask_afm_question(question, context, api_key):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://your-project-url.com",  # Optional, change if deployed
        "X-Title": "AFM-GPT"
    }

    payload = {
        "model": "deepseek/deepseek-chat-v3-0324",
        "messages": [
            {
                "role": "system",
                "content": "You are an expert in AFM (Atomic Force Microscopy). Answer questions simply."
            },
            {
                "role": "user",
                "content": f"Surface summary: {context}\nQuestion: {question}"
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ Error from OpenRouter API: {response.text}"
