import math
import torch

def roi_pooling(features: torch.Tensor, rois: torch.Tensor,
                output_size: tuple[int, int]) -> torch.Tensor:
    """RoI Pooling。

    features: (C, H, W)，rois: (N, 4)，output_size: (out_h, out_w)。
    返回: (N, C, out_h, out_w)。
    """
    out_h, out_w = output_size
    c, h, w = features.shape
    n = rois.shape[0]
    out = torch.zeros(n, c, out_h, out_w)

    for i, roi in enumerate(rois):
        x1, y1, x2, y2 = roi.tolist()
        roi_h = max(y2 - y1, 1e-6)
        roi_w = max(x2 - x1, 1e-6)
        for ph in range(out_h):
            y_start = max(0, min(h, math.floor(y1 + ph * roi_h / out_h)))
            y_end = max(0, min(h, math.ceil(y1 + (ph + 1) * roi_h / out_h)))
            y_end = max(y_end, y_start + 1) if y_start < h else h
            for pw in range(out_w):
                x_start = max(0, min(w, math.floor(x1 + pw * roi_w / out_w)))
                x_end = max(0, min(w, math.ceil(x1 + (pw + 1) * roi_w / out_w)))
                x_end = max(x_end, x_start + 1) if x_start < w else w
                if y_start >= h or x_start >= w:
                    continue
                patch = features[:, y_start:y_end, x_start:x_end]
                if patch.numel() > 0:
                    out[i, :, ph, pw] = patch.reshape(c, -1).max(dim=1).values
    return out
