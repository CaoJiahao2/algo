import torch
import torch.nn.functional as F

def init_kv_cache(batch_size: int, num_heads: int, max_len: int, d_k: int) -> dict:
    return {
        'k': torch.zeros(batch_size, num_heads, max_len, d_k),
        'v': torch.zeros(batch_size, num_heads, max_len, d_k),
        'pos': 0,
    }

def update_kv_cache(cache: dict, k: torch.Tensor, v: torch.Tensor) -> dict:
    pos = cache['pos']
    cache['k'][:, :, pos:pos + k.size(2)] = k
    cache['v'][:, :, pos:pos + v.size(2)] = v
    cache['pos'] += k.size(2)
    return cache

def attention_with_cache(q: torch.Tensor, cache: dict) -> torch.Tensor:
    pos = cache['pos']
    k = cache['k'][:, :, :pos]
    v = cache['v'][:, :, :pos]
    scores = torch.matmul(q, k.transpose(-2, -1)) / (q.size(-1) ** 0.5)
    weights = F.softmax(scores, dim=-1)
    return torch.matmul(weights, v)

