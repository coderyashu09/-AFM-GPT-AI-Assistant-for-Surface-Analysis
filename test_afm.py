import requests
import json

def ask_afm_question(question, context, api_key):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://your-project-url.com",  # Optional
        "X-Title": "AFM Assistant"
    }

    payload = {
        "model": "deepseek/deepseek-chat-v3-0324",
        "messages": [
            {
                "role": "system",
                "content": "You are an expert in AFM (Atomic Force Microscopy). Give easy explanations."
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


# Example usage
api_key = "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"  # ✅ Your new key
question = "What does roughness tell us about this surface?"
context = "The AFM image shows nanoscale bumps and valleys."

response = ask_afm_question(question, context, api_key)
print("🤖 AI Answer:")
print(response)
