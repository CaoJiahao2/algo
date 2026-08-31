import torch
from typing import Callable

def ddim_sampling(eps_model: Callable, shape: tuple[int, ...], betas: torch.Tensor, eta: float = 0.0) -> torch.Tensor:
    T = len(betas)
    alphas = 1.0 - betas
    alpha_bar = torch.cumprod(alphas, dim=0)
    x = torch.randn(shape)
    for t in reversed(range(T)):
        t_tensor = torch.full((shape[0],), t, dtype=torch.long)
        eps = eps_model(x, t_tensor)
        alpha_bar_t = alpha_bar[t]
        alpha_bar_prev = alpha_bar[t - 1] if t > 0 else torch.tensor(1.0)
        x0_pred = (x - torch.sqrt(1 - alpha_bar_t) * eps) / torch.sqrt(alpha_bar_t)
        sigma = eta * torch.sqrt((1 - alpha_bar_prev) / (1 - alpha_bar_t) * (1 - alpha_bar_t / alpha_bar_prev))
        direction = torch.sqrt(1 - alpha_bar_prev - sigma ** 2) * eps
        noise = torch.randn_like(x) if eta > 0 else torch.zeros_like(x)
        x = torch.sqrt(alpha_bar_prev) * x0_pred + direction + sigma * noise
    return x

