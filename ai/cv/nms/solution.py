import torch
from ai.cv.iou.solution import iou

def nms(boxes: torch.Tensor, scores: torch.Tensor, iou_threshold: float) -> torch.Tensor:
    """非极大值抑制。

    boxes: (N, 4)，scores: (N,)，iou_threshold: 重叠抑制阈值。
    返回: 保留下来的框索引（按分数从高到低）。
    """
    if boxes.numel() == 0:
        return torch.empty(0, dtype=torch.long)

    order = scores.argsort(descending=True)
    keep = []
    while order.numel() > 0:
        idx = order[0].item()
        keep.append(idx)
        if order.numel() == 1:
            break
        rest = order[1:]
        ious = iou(boxes[rest], boxes[idx:idx + 1]).squeeze(-1)
        order = rest[ious <= iou_threshold]
    return torch.tensor(keep, dtype=torch.long)
