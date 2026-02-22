import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModel

class SentenceEmbedder(nn.Module):
    def __init__(self, model_name='bert-base-uncased'):
        super().__init__()
        self.encoder = AutoModel.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    def mean_pooling(self, model_output, attention_mask):
        #broadcast by unsqueezing mask and applying mask to model_output
        token_embeddings = model_output.last_hidden_state
        input_mask_expanded = attention_mask.unsqueeze(-1).float()

        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    def max_pooling(self, model_output, attention_mask):
        token_embeddings = model_output.last_hidden_state

        #set padding tokens to large negative number so they don't affect max
        input_mask_expanded = attention_mask.unsqueeze(-1).float()
        token_embeddings[input_mask_expanded == 0] = -1e9

        return torch.max(token_embeddings, dim=1).values

    def forward(self, input):
        encoded = self.tokenizer(input, padding=True, truncation=True, return_tensors='pt')

        with torch.no_grad():
            output = self.encoder(**encoded)
            #use either max_pooling or mean_pooling. test both methodologies and use the one with higher accuracy
            return self.mean_pooling(output, encoded['attention_mask'])