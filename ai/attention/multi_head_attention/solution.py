import math
import torch
import torch.nn as nn


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()

        assert d_model % num_heads == 0

        self.d_model = d_model
        self.num_heads = num_heads
        self.d_head = d_model // num_heads

        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)

    def forward(self, x, mask=None):
        """
        x: [B, L, D]
        mask: broadcastable to [B, H, L, L]
        """

        B, L, _ = x.shape

        # 1. linear projection
        Q = self.W_q(x)  # [B, L, D]
        K = self.W_k(x)
        V = self.W_v(x)

        # 2. split heads
        # [B, L, D] -> [B, H, L, d]
        Q = Q.view(B, L, self.num_heads, self.d_head).transpose(1, 2)
        K = K.view(B, L, self.num_heads, self.d_head).transpose(1, 2)
        V = V.view(B, L, self.num_heads, self.d_head).transpose(1, 2)

        # 3. scaled dot-product attention
        # [B, H, L, d] @ [B, H, d, L]
        # -> [B, H, L, L]
        scores = Q @ K.transpose(-2, -1)
        scores = scores / math.sqrt(self.d_head)

        # 4. mask
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float("-inf"))

        # 5. softmax
        attn = torch.softmax(scores, dim=-1)

        # 6. weighted sum
        # [B, H, L, L] @ [B, H, L, d]
        # -> [B, H, L, d]
        out = attn @ V

        # 7. concat heads
        # [B, H, L, d] -> [B, L, H, d] -> [B, L, D]
        out = out.transpose(1, 2).contiguous()
        out = out.view(B, L, self.d_model)

        # 8. output projection
        out = self.W_o(out)

        return out