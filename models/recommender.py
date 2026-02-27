import torch
import pandas as pd
from .SentenceEmbedder import SentenceEmbedder
from .similarity import top_k_similar

import os

class Recommender:
    #model_name should be changed to "sentence-transformers/all-MiniLM-L6-v2" for higher accuracy
    #second option is ber-base-uncased but its too large for render
    def __init__(self, data_path, cache_path="data/embeddings.pt", model_name='sentence-transformers/all-MiniLM-L6-v2'):
        self.embedder = SentenceEmbedder(model_name)
        self.df = pd.read_csv(data_path)
        self.embeddings = None
        self._embed_dataset(cache_path)
    
    def _embed_dataset(self, cache_path, batch_size=32):
        if os.path.exists(cache_path):
            #load cached embeddings if exists
            self.embeddings = torch.load(cache_path)
        else:
            #get all descriptions, fill missing with empty string
            descriptions = self.df['description'].fillna('').tolist()
            all_embeddings = []

            #had to use batches bcs embedding the entire csv file in one go allocated too many resources at a time
            for i in range(0, len(descriptions), batch_size):
                batch = descriptions[i: i+batch_size]
                embeddings = self.embedder(batch)
                all_embeddings.append(embeddings)

            self.embeddings = torch.cat(all_embeddings, dim=0)
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