import torch
import torch.nn.functional as F

def convolution2d(x: torch.Tensor, kernel: torch.Tensor,
                  stride: int = 1, padding: int = 0) -> torch.Tensor:
    """朴素 2D 卷积。

    x: (C_in, H, W)，kernel: (C_out, C_in, KH, KW)。
    返回: (C_out, H_out, W_out)。
    """
    c_in, h, w = x.shape
    c_out, _, kh, kw = kernel.shape

    if padding > 0:
        x = F.pad(x, (padding, padding, padding, padding))

    h_out = (h + 2 * padding - kh) // stride + 1
    w_out = (w + 2 * padding - kw) // stride + 1
    out = torch.zeros(c_out, h_out, w_out)

    for co in range(c_out):
        for i in range(h_out):
            for j in range(w_out):
                patch = x[:, i * stride:i * stride + kh, j * stride:j * stride + kw]
                out[co, i, j] = (patch * kernel[co]).sum()
    return out
