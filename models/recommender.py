import torch
import pandas as pd
from models.SentenceEmbedder import SentenceEmbedder
from models.similarity import top_k_similar

import os

class Recommender:
    def __init__(self, data_path, cache_path="data/embeddings.pt", model_name='bert-base-uncased'):
        self.embedder = SentenceEmbedder(model_name)
        self.df = pd.read_csv(data_path)
        self.embeddings = None
        self._embed_dataset(cache_path)
    
    def _embed_dataset(self, cache_path):
        if os.path.exists(cache_path):
            #load cached embeddings if exists
            self.embeddings = torch.load(cache_path)
        else:
            #get all descriptions, fill missing with empty string
            descriptions = self.df['description'].fillna('').tolist()
            self.embeddings = self.embedder(descriptions)
            torch.save(self.embeddings, cache_path)
        
    def recommend(self, show_name, k=5):
        #find show in the dataset
        row = self.df[self.df['title'].str.lower() == show_name.lower()]
        if row.empty:
            raise Exception("Can't find show bud")
        
        idx = row.index[0]
        query_embedding = self.embeddings[idx].unsqueeze(0)

        indices, scores = top_k_similar(query_embedding, self.embeddings, k=k+1)

        results = []
        for i, score in zip(indices[0], scores[0]):
            if i.item() == idx:
                continue

            results.append({
                'title': self.df.iloc[i.item()]['title'],
                'score': round(score.item(), 3)
            })
        return results[:k]