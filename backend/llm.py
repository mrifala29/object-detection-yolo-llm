import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.1:8b"

def explain(context, objects):
    prompt = f"""
You are an AI assistant.
Explain the following detected objects in simple and clear terms.

Detected objects:
{objects}

Context information:
{context}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]
