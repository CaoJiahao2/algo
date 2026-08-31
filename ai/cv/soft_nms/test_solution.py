import torch
from ai.cv.soft_nms.solution import soft_nms

def test_soft_nms_keeps_single_dominant_box():
    boxes = torch.tensor([[0.0, 0.0, 1.0, 1.0], [0.0, 0.0, 1.0, 1.0]])
    scores = torch.tensor([0.9, 0.8])
    keep = soft_nms(boxes, scores, score_threshold=0.2)
    assert keep.tolist() == [0]

def test_soft_nms_decays_but_can_keep_strong_second_box():
    # 高分框与低分框重叠不大，低分框分数足够高，二者都应保留。
    boxes = torch.tensor([[0.0, 0.0, 2.0, 2.0], [1.5, 0.0, 3.0, 2.0]])
    scores = torch.tensor([0.9, 0.85])
    keep = soft_nms(boxes, scores, iou_threshold=0.5, sigma=0.3, score_threshold=0.1)
    assert len(keep) == 2
