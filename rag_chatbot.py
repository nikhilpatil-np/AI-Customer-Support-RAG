import faiss
import numpy as np


class VectorStore:

    def __init__(self):
        self.index = None

    def create_index(self, embeddings):
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(embeddings))

        print(f"FAISS index created successfully.")
        print(f"Total vectors stored: {self.index.ntotal}")

    def search(self, query_embedding, top_k=3):
        distances, indices = self.index.search(query_embedding, top_k)
        return distances, indices

    def save_index(self, path):
        faiss.write_index(self.index, path)

    def load_index(self, path):
        self.index = faiss.read_index(path)

        print("FAISS index loaded successfully.")