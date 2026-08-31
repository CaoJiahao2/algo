# Softmax

## 题目
实现稳定的 softmax：将 logits 转换为和为 1 的概率分布。

## 思路
先减去最大值避免上溢，再做指数归一化。

## 复杂度
- 时间：O(n)
- 空间：O(n)

## 代码
见 [solution.py](solution.py)

