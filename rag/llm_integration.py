from transformers import pipeline

llm = pipeline("text-generation", model="gpt2")

def generate_answer(context, query):
    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    return llm(prompt, max_length=200)[0]['generated_text']