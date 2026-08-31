# Gradient Descent

## 题目
用梯度下降最小化 `f(x) = (x - a)^2`。

## 思路
求导 `f'(x) = 2(x - a)`，迭代 `x -= lr * grad`。

## 复杂度
- 时间：O(steps)
- 空间：O(1)

## 代码
见 [solution.py](solution.py)

