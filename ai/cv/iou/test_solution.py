import torch
from ai.cv.iou.solution import iou

def test_iou_overlap_half():
    a = torch.tensor([[0.0, 0.0, 2.0, 2.0]])
    b = torch.tensor([[1.0, 0.0, 3.0, 2.0]])
    out = iou(a, b)
    assert out.shape == (1, 1)
    assert torch.isclose(out[0, 0], torch.tensor(1.0 / 3.0), atol=1e-6)

def test_iou_disjoint_and_identical():
    a = torch.tensor([[0.0, 0.0, 2.0, 2.0]])
    b = torch.tensor([[3.0, 3.0, 4.0, 4.0]])
    assert iou(a, b).item() == 0.0
    assert abs(iou(a, a).item() - 1.0) < 1e-6
