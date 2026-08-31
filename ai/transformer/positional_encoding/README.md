# Positional Encoding

## 题目
实现 Transformer 的正弦位置编码。

## 思路
偶数列用 sin、奇数列用 cos，频率随维度指数递减。

## 复杂度
- 时间：O(seq_len * d_model)
- 空间：O(seq_len * d_model)

## 代码
见 [solution.py](solution.py)

