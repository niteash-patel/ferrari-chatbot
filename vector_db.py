import numpy as np
import json
import chromadb
from sentence_transformers import SentenceTransformer

with open("ferrari_data.json","r", encoding="utf-8") as f:
    data=json.load(f)

embeddings=np.load("ferrari_embeddings.npy")

model = SentenceTransformer("all-MiniLM-L6-v2")

client=chromadb.Client()
collection=client.create_collection(name="ferrari_cars")

print("client and collection is ready")

documents=[car["summary"] for car in data]
metadatas=[{"model": car["model"], "image_url": car["image_url"] or""} for car in data]
ids=[str(i) for i in range(len(data))]

collection.add(
    documents=documents,
    embeddings=embeddings.tolist(),
    metadatas=metadatas,
    ids=ids
)

print("data add into collection")
print(collection.count())

query = "Ferrari Luce electric car"
query_embedding = model.encode([query])

results = collection.query(
    query_embeddings=query_embedding.tolist(),
    n_results=3
)

print(results["documents"])
print(results["metadatas"])