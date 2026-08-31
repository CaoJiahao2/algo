import torch
from ai.diffusion.ddpm_forward_diffusion.solution import ddpm_forward_diffusion

def test_forward_shape():
    torch.manual_seed(0)
    betas = torch.linspace(0.0001, 0.02, 100)
    x0 = torch.randn(2, 4)
    t = torch.tensor([0, 50])
    xt, eps = ddpm_forward_diffusion(x0, t, betas)
    assert xt.shape == (2, 4)
    assert eps.shape == (2, 4)

