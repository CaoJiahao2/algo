# Classifier-Free Guidance

## 题目
实现无分类器引导：组合条件与无条件噪声预测。

## 思路
`eps = eps_uncond + w * (eps_cond - eps_uncond)`。

## 复杂度
- 时间：O(n)
- 空间：O(n)

## 代码
见 [solution.py](solution.py)

