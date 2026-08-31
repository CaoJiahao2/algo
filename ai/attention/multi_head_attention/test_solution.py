import torch
from ai.attention.multi_head_attention.solution import MultiHeadAttention

def test_mha_shape():
    torch.manual_seed(0)
    mha = MultiHeadAttention(8, 2)
    x = torch.randn(2, 5, 8)
    out = mha(x, x, x)
    assert out.shape == (2, 5, 8)
    assert torch.isfinite(out).all()

