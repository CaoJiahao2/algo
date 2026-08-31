import torch
from ai.transformer.kv_cache.solution import init_kv_cache, update_kv_cache, attention_with_cache

def test_kv_cache():
    torch.manual_seed(0)
    cache = init_kv_cache(1, 2, 8, 4)
    k = torch.randn(1, 2, 2, 4)
    v = torch.randn(1, 2, 2, 4)
    update_kv_cache(cache, k, v)
    assert cache['pos'] == 2
    q = torch.randn(1, 2, 1, 4)
    out = attention_with_cache(q, cache)
    assert out.shape == (1, 2, 1, 4)

