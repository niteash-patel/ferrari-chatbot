import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
from sentence_transformers import SentenceTransformer
import json
import numpy as np
import chromadb

load_dotenv()

st.markdown("""""", unsafe_allow_html=True)

with open("ferrari_data.json","r", encoding="utf-8") as f:
    data=json.load(f)

embeddings=np.load("ferrari_embeddings.npy")

model=SentenceTransformer("all-MiniLM-L6-v2")

db_client=chromadb.Client()
collection=db_client.get_or_create_collection(name="ferrari_cars")

documents=[car["summary"] for car in data]
metadatas=[{"model": car["model"], "image_url": car["image_url"] or ""} for car in data]
ids=[str(i) for i in range(len(data))]

collection.add(
    documents=documents,
    embeddings=embeddings.tolist(),
    metadatas=metadatas,
    ids=ids
)

st.markdown("""
<style>
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}

.stApp {
    background: linear-gradient(135deg, #1a0000 0%, #2b0000 50%, #000000 100%);
}

h1 {
    animation: fadeIn 1s ease-in-out;
    color: #ff2800 !important;
    text-shadow: 0 0 15px rgba(255, 40, 0, 0.6);
}

div.stButton > button {
    background: linear-gradient(90deg, #ff2800, #b30000);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 24px;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(255, 40, 0, 0.4);
}

div.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 20px rgba(255, 40, 0, 0.7);
}

div[data-testid="stTextInput"] input {
    border: 2px solid #ff2800;
    border-radius: 8px;
    animation: fadeIn 1.2s ease-in-out;
}

div[data-testid="stMarkdownContainer"] {
    animation: fadeIn 0.8s ease-in-out;
}
</style>
""", unsafe_allow_html=True)

st.title("🏎️ Ferrari Car Chatbot")
st.write("Ask me anything about Ferrari cars!")

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)
query=st.text_input("Your question:")

generate_clicked = st.button("Generate")

if query and generate_clicked:

    query_embedding=model.encode([query])
    results=collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=3
    )
    context_text = "\n\n".join(results["documents"][0])

    response=client.chat.completions.create(
        model="meta/llama-3.1-70b-instruct",
        max_tokens=300,
        messages=[
            {"role":"user", "content": f"Use this information to answer:\n\n{context_text}\n\nQuestion: {query}"}
        ]
    )
    st.write(response.choices[0].message.content)

    top_image = results["metadatas"][0][0]["image_url"]
    if top_image:
        st.image(top_image, caption=results["metadatas"][0][0]["model"])
