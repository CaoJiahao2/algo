import torch
import torch.nn.functional as F
from ai.cv.max_pooling2d.solution import max_pooling2d

def test_max_pooling_matches_pytorch():
    torch.manual_seed(0)
    x = torch.randn(2, 6, 6)
    out = max_pooling2d(x, kernel_size=2, stride=2, padding=0)
    ref = F.max_pool2d(x.unsqueeze(0), kernel_size=2, stride=2).squeeze(0)
    assert out.shape == ref.shape
    assert torch.allclose(out, ref, atol=1e-6)

def test_max_pooling_with_padding():
    torch.manual_seed(1)
    x = torch.randn(1, 5, 5)
    out = max_pooling2d(x, kernel_size=3, stride=2, padding=1)
    ref = F.max_pool2d(x.unsqueeze(0), kernel_size=3, stride=2, padding=1).squeeze(0)
    assert out.shape == ref.shape
    assert torch.allclose(out, ref, atol=1e-6)
