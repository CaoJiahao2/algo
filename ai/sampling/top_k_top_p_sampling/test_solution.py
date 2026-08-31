import torch
from ai.sampling.top_k_top_p_sampling.solution import top_k_top_p_sampling

def test_top_k_sampling():
    torch.manual_seed(0)
    logits = torch.tensor([[0.1, 0.2, 10.0, 0.3]])
    out = top_k_top_p_sampling(logits, top_k=1)
    assert out.item() == 2

def test_shape():
    torch.manual_seed(1)
    logits = torch.randn(2, 5)
    out = top_k_top_p_sampling(logits, top_k=2, top_p=0.9)
    assert out.shape == (2,)

