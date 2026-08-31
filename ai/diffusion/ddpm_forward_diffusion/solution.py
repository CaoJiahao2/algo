import torch

def ddpm_forward_diffusion(x0: torch.Tensor, t: torch.Tensor, betas: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    alphas = 1.0 - betas
    alpha_bar = torch.cumprod(alphas, dim=0)
    at = alpha_bar[t]
    eps = torch.randn_like(x0)
    shape = (1,) * (x0.dim() - 1)
    xt = at.view(-1, *shape).sqrt() * x0 + (1 - at).view(-1, *shape).sqrt() * eps
    return xt, eps

