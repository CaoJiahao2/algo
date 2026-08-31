import torch
from typing import Callable, Optional

def greedy_decoding(logits_fn: Callable[[torch.Tensor], torch.Tensor], start_token: int,
                    max_length: int, eos_token: Optional[int] = None) -> list[int]:
    seq = [start_token]
    for _ in range(max_length):
        logits = logits_fn(torch.tensor(seq))
        next_token = int(torch.argmax(logits[-1]).item())
        seq.append(next_token)
        if next_token == eos_token:
            break
    return seq

