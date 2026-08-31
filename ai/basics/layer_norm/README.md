# Layer Normalization

## 题目
实现对最后一维的 LayerNorm 前向计算。

## 思路
沿最后一维求均值和方差，标准化后（训练时还需乘加可学习参数）。

## 复杂度
- 时间：O(n)
- 空间：O(n)

## 代码
见 [solution.py](solution.py)

