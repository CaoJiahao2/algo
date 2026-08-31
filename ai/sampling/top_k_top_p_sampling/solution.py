import torch
import torch.nn.functional as F

def top_k_top_p_sampling(logits: torch.Tensor, top_k: int = 0, top_p: float = 1.0,
                         temperature: float = 1.0) -> torch.Tensor:
    logits = logits / temperature
    if top_k > 0:
        topk = torch.topk(logits, min(top_k, logits.size(-1)))
        mask = torch.full_like(logits, float('-inf'))
        mask.scatter_(-1, topk.indices, topk.values)
        logits = mask

    probs = F.softmax(logits, dim=-1)
    sorted_probs, sorted_indices = torch.sort(probs, descending=True)
    cumsum = torch.cumsum(sorted_probs, dim=-1)
    keep = (cumsum - sorted_probs) < top_p
    keep[..., 0] = True
    filtered = sorted_probs * keep
    filtered = filtered / filtered.sum(dim=-1, keepdim=True)
    sampled = torch.multinomial(filtered, 1)
    return sorted_indices.gather(-1, sampled).squeeze(-1)

