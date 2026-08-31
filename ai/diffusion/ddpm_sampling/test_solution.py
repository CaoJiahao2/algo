import torch
from ai.diffusion.ddpm_sampling.solution import ddpm_sampling

def test_ddpm_sampling_shape():
    torch.manual_seed(0)
    betas = torch.linspace(0.0001, 0.02, 10)
    def eps_model(x, t):
        return torch.zeros_like(x)
    out = ddpm_sampling(eps_model, (2, 4), betas)
    assert out.shape == (2, 4)
    assert torch.isfinite(out).all()

