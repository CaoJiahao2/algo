import torch
from ai.attention.scaled_dot_product_attention.solution import scaled_dot_product_attention

def test_attention_shape():
    torch.manual_seed(0)
    q = torch.randn(2, 3, 8)
    k = torch.randn(2, 5, 8)
    v = torch.randn(2, 5, 8)
    out = scaled_dot_product_attention(q, k, v)
    assert out.shape == (2, 3, 8)

def test_attention_mask():
    torch.manual_seed(0)
    q = torch.randn(1, 2, 4)
    k = torch.randn(1, 3, 4)
    v = torch.randn(1, 3, 4)
    mask = torch.tensor([[1, 1, 0]])
    out = scaled_dot_product_attention(q, k, v, mask=mask)
    assert torch.isfinite(out).all()

