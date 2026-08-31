import torch
from ai.diffusion.classifier_free_guidance.solution import classifier_free_guidance

def test_cfg():
    cond = torch.tensor([1.0, 2.0])
    uncond = torch.tensor([0.0, 0.0])
    out = classifier_free_guidance(cond, uncond, 7.5)
    assert torch.allclose(out, torch.tensor([7.5, 15.0]))

