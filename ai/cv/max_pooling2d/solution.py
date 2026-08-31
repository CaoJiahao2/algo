import torch
import torch.nn.functional as F

def max_pooling2d(x: torch.Tensor, kernel_size: int,
                  stride: int | None = None, padding: int = 0) -> torch.Tensor:
    """朴素 2D 最大池化。

    x: (C, H, W)，kernel_size: 正方形窗口边长。
    返回: (C, H_out, W_out)。
    """
    stride = kernel_size if stride is None else stride
    c, h, w = x.shape
    if padding > 0:
        x = F.pad(x, (padding, padding, padding, padding), value=float('-inf'))

    h_out = (h + 2 * padding - kernel_size) // stride + 1
    w_out = (w + 2 * padding - kernel_size) // stride + 1
    out = torch.zeros(c, h_out, w_out)

    for i in range(h_out):
        for j in range(w_out):
            patch = x[:, i * stride:i * stride + kernel_size, j * stride:j * stride + kernel_size]
            out[:, i, j] = patch.amax(dim=(1, 2))
    return out
