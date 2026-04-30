from fastapi import FastAPI
from rag_pipeline import retrieve, generate_answer

app = FastAPI()

@app.get("/query")
def query(q: str):
    context = retrieve(q, model, index, chunks)
    answer = generate_answer(context, q)
    return {"response": answer}