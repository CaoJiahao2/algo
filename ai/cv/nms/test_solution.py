import torch
from ai.cv.nms.solution import nms

def test_nms_suppresses_duplicate_box():
    boxes = torch.tensor([[0.0, 0.0, 1.0, 1.0], [0.0, 0.0, 1.0, 1.0]])
    scores = torch.tensor([0.9, 0.8])
    keep = nms(boxes, scores, iou_threshold=0.5)
    assert keep.tolist() == [0]

def test_nms_keeps_separated_boxes():
    boxes = torch.tensor([[0.0, 0.0, 1.0, 1.0], [2.0, 2.0, 3.0, 3.0]])
    scores = torch.tensor([0.6, 0.9])
    keep = nms(boxes, scores, iou_threshold=0.5)
    assert keep.tolist() == [1, 0]
