import torch

def classifier_free_guidance(eps_cond: torch.Tensor, eps_uncond: torch.Tensor, guidance_scale: float) -> torch.Tensor:
    return eps_uncond + guidance_scale * (eps_cond - eps_uncond)

