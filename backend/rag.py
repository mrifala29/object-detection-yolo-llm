import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class RAG:
    def __init__(self, path="data/objects.txt"):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        self.texts = []
        with open(path, 'r') as f:
            for line in f:
                self.text.append(line.strip())
                
        embeddings = self.model.encode(self.texts)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(embeddings))
        
    def search(self, query):
        q_emb = self.model.encode([query])
        _, idx = self.index.search(np.array(q_emb), 1)
        return self.texts[idx[0][0]]