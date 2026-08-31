import torch
from ai.sampling.beam_search.solution import beam_search

def test_beam_search():
    def logits_fn(seq):
        logits = torch.zeros(len(seq), 3)
        logits[-1, 1] = 5.0
        return logits
    assert beam_search(logits_fn, 0, 2, 5) == [0, 1, 1, 1, 1, 1]

