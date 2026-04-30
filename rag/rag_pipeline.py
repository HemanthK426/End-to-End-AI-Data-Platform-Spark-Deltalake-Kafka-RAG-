def retrieve(query, model, index, chunks):
    query_embedding = model.encode([query])
    D, I = index.search(query_embedding, k=3)
    return [chunks[i] for i in I[0]]