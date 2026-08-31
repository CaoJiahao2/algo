import torch
from typing import Callable

def ddpm_sampling(eps_model: Callable, shape: tuple[int, ...], betas: torch.Tensor) -> torch.Tensor:
    T = len(betas)
    alphas = 1.0 - betas
    alpha_bar = torch.cumprod(alphas, dim=0)
    x = torch.randn(shape)
    for t in reversed(range(T)):
        t_tensor = torch.full((shape[0],), t, dtype=torch.long)
        eps = eps_model(x, t_tensor)
        alpha_t = alphas[t]
        alpha_bar_t = alpha_bar[t]
        beta_t = betas[t]
        noise = torch.randn_like(x) if t > 0 else torch.zeros_like(x)
        x = (1 / torch.sqrt(alpha_t)) * (x - ((1 - alpha_t) / torch.sqrt(1 - alpha_bar_t)) * eps) + torch.sqrt(beta_t) * noise
    return x

