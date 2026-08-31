import torch
import torch.nn.functional as F
from ai.cv.convolution2d.solution import convolution2d

def test_convolution_matches_pytorch():
    torch.manual_seed(0)
    x = torch.randn(3, 7, 7)
    kernel = torch.randn(2, 3, 3, 3)
    out = convolution2d(x, kernel, stride=1, padding=1)
    ref = F.conv2d(x.unsqueeze(0), kernel, stride=1, padding=1).squeeze(0)
    assert out.shape == ref.shape
    assert torch.allclose(out, ref, atol=1e-5)

def test_convolution_stride2_shape():
    torch.manual_seed(1)
    x = torch.randn(2, 6, 6)
    kernel = torch.randn(4, 2, 3, 3)
    out = convolution2d(x, kernel, stride=2, padding=0)
    assert out.shape == (4, 2, 2)
