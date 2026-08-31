# Top-K & Top-P Sampling

## 题目
实现带温度、top-k 与 top-p（nucleus）过滤的采样。

## 思路
先温度缩放，top-k 截断，再按累积概率 top-p 过滤后重新归一化，最后多项式采样。

## 复杂度
- 时间：O(V log V)
- 空间：O(V)

## 代码
见 [solution.py](solution.py)

