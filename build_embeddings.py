import json
from sentence_transformers import SentenceTransformer
import numpy as np

with open("ferrari_data.json","r", encoding="utf-8") as f:
    data=json.load(f)

model=SentenceTransformer("all-MiniLM-L6-v2")
summaries=[car["summary"] for car in data]

embeddings=model.encode(summaries)

print(len(embeddings))
print(embeddings.shape)

np.save("ferrari_embeddings.npy", embeddings)

print("Embeddings saved!")