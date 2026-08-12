from sentence_transformers import SentenceTransformer

model=SentenceTransformer("all-MiniLM-L6-v2")

sentence1="Ferrari is a fast sports car"
sentence2 = "Ferrari makes speedy racing vehicles"
sentence3 = "I like eating pizza"

embedding1=model.encode(sentence1)
embedding2=model.encode(sentence2)
embedding3=model.encode(sentence3)

similarity_1_2=model.similarity(embedding1,embedding2)
similarity_1_3=model.similarity(embedding1,embedding3)

print("Sentence 1 vs 2 (similar meaning):", similarity_1_2)
print("Sentence 1 vs 3 (different meaning):", similarity_1_3)