import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

def explain(context, objects):
    prompt = f"""
You MUST use the following context to answer.
If the information is not in the context, say you don't know.

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

    data = response.json()

    print("OLLAMA RAW RESPONSE:", data)

    if "response" in data:
        return data["response"]

    if "message" in data and "content" in data["message"]:
        return data["message"]["content"]

    return "LLM did not return a valid response."
