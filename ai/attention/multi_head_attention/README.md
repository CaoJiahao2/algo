# Multi-Head Attention

## 题目
实现多头注意力：将 Q/K/V 投影后拆成多个头，各自做缩放点积注意力，再拼接投影输出。

## 思路
按 `d_k = d_model / num_heads` 拆分，并行计算后 transpose 合并，最后输出投影。

## 复杂度
- 时间：O(T^2 d)
- 空间：O(T^2)

## 代码
见 [solution.py](solution.py)

