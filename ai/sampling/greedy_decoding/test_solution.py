import torch
from ai.sampling.greedy_decoding.solution import greedy_decoding

def test_greedy_decoding():
    def logits_fn(seq):
        logits = torch.zeros(len(seq), 3)
        logits[-1, 1] = 5.0
        return logits
    assert greedy_decoding(logits_fn, 0, 5) == [0, 1, 1, 1, 1, 1]

def test_greedy_decoding_eos():
    def logits_fn(seq):
        logits = torch.zeros(len(seq), 3)
        logits[-1, 2] = 5.0
        return logits
    assert greedy_decoding(logits_fn, 0, 10, eos_token=2) == [0, 2]

