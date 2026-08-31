import torch

def iou(boxes1: torch.Tensor, boxes2: torch.Tensor) -> torch.Tensor:
    """计算两组框的 IoU。

    boxes1: (N, 4)，boxes2: (M, 4)，坐标 [x1, y1, x2, y2]。
    返回: (N, M) 的 IoU 矩阵。
    """
    lt = torch.max(boxes1[:, None, :2], boxes2[None, :, :2])
    rb = torch.min(boxes1[:, None, 2:], boxes2[None, :, 2:])
    inter_wh = (rb - lt).clamp(min=0.0)
    inter = inter_wh[..., 0] * inter_wh[..., 1]

    area1 = (boxes1[:, 2] - boxes1[:, 0]).clamp(min=0.0) * (boxes1[:, 3] - boxes1[:, 1]).clamp(min=0.0)
    area2 = (boxes2[:, 2] - boxes2[:, 0]).clamp(min=0.0) * (boxes2[:, 3] - boxes2[:, 1]).clamp(min=0.0)
    union = area1[:, None] + area2[None, :] - inter
    return inter / (union + 1e-8)
