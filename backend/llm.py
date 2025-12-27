import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def explain(context, objects):
    prompt = f"""
You are an AI assistant.

Explain the following detected objects in simple and clear language.
Focus on what the objects are commonly used for.

Detected objects: {objects}

Knowledge context:
{context}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]
