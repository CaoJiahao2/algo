# Greedy Decoding

## 题目
实现自回归贪心解码：每一步取 logits 中概率最大的 token。

## 思路
给定 `logits_fn(seq)` 返回下一步 logits，取 argmax 直到达到最大长度或遇到 EOS。

## 复杂度
- 时间：O(max_len * V)
- 空间：O(max_len)

## 代码
见 [solution.py](solution.py)

