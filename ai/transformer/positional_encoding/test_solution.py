import torch
from ai.transformer.positional_encoding.solution import positional_encoding

def test_pe_shape():
    pe = positional_encoding(10, 16)
    assert pe.shape == (10, 16)
    assert torch.allclose(pe[:, 0], torch.sin(torch.arange(10, dtype=torch.float32)))

