# DDIM Sampling

## 题目
实现 DDIM 反向采样（默认确定性采样，eta=0）。

## 思路
由 x_t 预测 x0，再按 alpha_bar 递推 x_{t-1}，eta 控制随机性。

## 复杂度
- 时间：O(T * model_cost)
- 空间：O(x)

## 代码
见 [solution.py](solution.py)

