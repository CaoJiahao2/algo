import torch
from typing import Callable, Optional

def beam_search(logits_fn: Callable[[torch.Tensor], torch.Tensor], start_token: int,
                beam_width: int, max_length: int, eos_token: Optional[int] = None) -> list[int]:
    beams: list[tuple[float, list[int]]] = [(0.0, [start_token])]
    for _ in range(max_length):
        candidates: list[tuple[float, list[int]]] = []
        for score, seq in beams:
            if seq[-1] == eos_token:
                candidates.append((score, seq))
                continue
            logits = logits_fn(torch.tensor(seq))
            log_probs = torch.log_softmax(logits[-1], dim=-1)
            topk = torch.topk(log_probs, beam_width)
            for lp, tok in zip(topk.values.tolist(), topk.indices.tolist()):
                candidates.append((score + lp, seq + [tok]))
        beams = sorted(candidates, key=lambda x: -x[0])[:beam_width]
    return beams[0][1]

