import torch
import torch.nn.functional as F

def cosine_similarity(embedding_1, embedding_2):
    embedding_1 = F.normalize(embedding_1, p=2, dim=-1)
    embedding_2 = F.normalize(embedding_2, p=2, dim=-1)

    return torch.sum(embedding_1 * embedding_2, dim=-1)

def top_k_similar(query_embedding, all_embeddings, k=5):
    query_embedding = F.normalize(query_embedding, p=2, dim=-1)
    all_embeddings = F.normalize(all_embeddings, p=2, dim=-1)

    similarities = torch.matmul(query_embedding, all_embeddings.T)

    scores, indices = torch.topk(similarities, k)

    return indices, scores