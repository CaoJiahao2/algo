import torch
from ai.cv.roi_pooling.solution import roi_pooling

def test_roi_pooling_shape():
    torch.manual_seed(0)
    features = torch.randn(4, 8, 8)
    rois = torch.tensor([[0.0, 0.0, 4.0, 4.0], [2.0, 2.0, 6.0, 6.0]])
    out = roi_pooling(features, rois, output_size=(2, 2))
    assert out.shape == (2, 4, 2, 2)

def test_roi_pooling_takes_bin_max():
    features = torch.zeros(1, 4, 4)
    features[0, 0, 0] = 5.0
    features[0, 3, 3] = 9.0
    rois = torch.tensor([[0.0, 0.0, 4.0, 4.0]])
    out = roi_pooling(features, rois, output_size=(2, 2))
    assert out[0, 0, 0, 0].item() == 5.0
    assert out[0, 0, 1, 1].item() == 9.0
