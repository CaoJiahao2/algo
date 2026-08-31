import torch
from ai.basics.layer_norm.solution import layer_norm

def test_layer_norm():
    torch.manual_seed(0)
    x = torch.randn(2, 3)
    out = layer_norm(x)
    assert out.shape == (2, 3)
    assert torch.allclose(out.mean(dim=-1), torch.zeros(2), atol=1e-4)
    assert torch.allclose(out.var(dim=-1, unbiased=False), torch.ones(2), atol=1e-4)

