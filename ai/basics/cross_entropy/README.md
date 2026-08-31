# Cross Entropy

## 题目
给定 logits 和真实类别下标，计算 softmax 交叉熵损失。

## 思路
log-sum-exp 技巧：先减最大值再算 log-softmax，取负真实类别的对数概率。

## 复杂度
- 时间：O(n)
- 空间：O(n)

## 代码
见 [solution.py](solution.py)

