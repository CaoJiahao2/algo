# Transformer Encoder Block

## 题目
实现一个 Transformer encoder 层：多头自注意力 + 残差 + LayerNorm，FFN + 残差 + LayerNorm。

## 思路
自注意力后接 Add & Norm，再经两层线性 FFN 后 Add & Norm。

## 复杂度
- 时间：O(T^2 d + T d_ff d)
- 空间：O(T^2)

## 代码
见 [solution.py](solution.py)

