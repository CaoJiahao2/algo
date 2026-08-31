import torch
from ai.diffusion.ddim_sampling.solution import ddim_sampling

def test_ddim_shape():
    torch.manual_seed(0)
    betas = torch.linspace(0.0001, 0.02, 10)
    def eps_model(x, t):
        return torch.zeros_like(x)
    out = ddim_sampling(eps_model, (2, 4), betas)
    assert out.shape == (2, 4)

