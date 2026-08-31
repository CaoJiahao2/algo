# Scaled Dot-Product Attention

## 题目
实现 `softmax(QK^T / sqrt(d_k)) V`，支持可选的 padding mask。

## 思路
缩放点积，mask 位置置 `-inf`，softmax 后加权求和。

## 复杂度
- 时间：O(T^2 d)
- 空间：O(T^2)

## 代码
见 [solution.py](solution.py)

