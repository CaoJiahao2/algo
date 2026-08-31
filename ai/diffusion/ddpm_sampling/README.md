# DDPM Sampling

## 题目
实现 DDPM 反向采样：从纯噪声出发，逐步用模型预测的噪声去噪。

## 思路
从 T-1 到 0 迭代，每一步按 DDPM 后验均值更新，非最后一步加随机噪声。

## 复杂度
- 时间：O(T * model_cost)
- 空间：O(x)

## 代码
见 [solution.py](solution.py)

