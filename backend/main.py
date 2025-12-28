from fastapi import FastAPI
from pydantic import BaseModel
from backend.rag import RAG
from backend.llm import explain

app = FastAPI()
rag = RAG()

class DetectRequest(BaseModel):
    objects: list[str]

@app.post("/explain")
def explain_objects(req: DetectRequest):
    explanations = []

    for obj in req.objects:
        context = rag.search(obj)
        explanations.append(context)

    final_explanation = explain(
        context=" ".join(explanations),
        objects=", ".join(req.objects)
    )

    print("\nAI Explanation:\n", final_explanation)
    return {"explanation": final_explanation}