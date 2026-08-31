import torch
from ai.cv.iou.solution import iou

def soft_nms(boxes: torch.Tensor, scores: torch.Tensor, iou_threshold: float = 0.5,
             sigma: float = 0.5, score_threshold: float = 0.001) -> torch.Tensor:
    """Soft NMS（高斯衰减版本）。

    boxes: (N, 4)，scores: (N,)。
    返回: 保留下来的框索引（按最终分数从高到低）。
    """
    if boxes.numel() == 0:
        return torch.empty(0, dtype=torch.long)

    bs = boxes.clone()
    ss = scores.clone()
    idxs = list(range(bs.shape[0]))
    keep = []

    while len(idxs) > 0:
        order = ss.argsort(descending=True)
        cur = order[0].item()
        keep.append(idxs[cur])
        if len(idxs) == 1:
            break

        ious = iou(bs, bs[cur].unsqueeze(0)).squeeze(-1)
        weights = torch.where(
            ious > iou_threshold,
            torch.exp(-(ious ** 2) / sigma),
            torch.ones_like(ss),
        )
        ss = ss * weights
        ss[cur] = 0.0

        remaining = (ss > score_threshold).nonzero(as_tuple=True)[0].tolist()
        idxs = [idxs[i] for i in remaining]
        bs = bs[remaining]
        ss = ss[remaining]

    return torch.tensor(keep, dtype=torch.long)
