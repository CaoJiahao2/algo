import torch
import torch.nn.functional as F

def scaled_dot_product_attention(query: torch.Tensor, key: torch.Tensor, value: torch.Tensor,
                                 mask: torch.Tensor | None = None) -> torch.Tensor:
    d_k = query.size(-1)
    scores = torch.matmul(query, key.transpose(-2, -1)) / (d_k ** 0.5)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float('-inf'))
    weights = F.softmax(scores, dim=-1)
    return torch.matmul(weights, value)

