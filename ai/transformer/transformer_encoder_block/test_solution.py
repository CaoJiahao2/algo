import torch
from ai.transformer.transformer_encoder_block.solution import TransformerEncoderBlock

def test_encoder_block():
    torch.manual_seed(0)
    block = TransformerEncoderBlock(8, 2, 32)
    x = torch.randn(2, 5, 8)
    out = block(x)
    assert out.shape == x.shape
    assert torch.isfinite(out).all()

