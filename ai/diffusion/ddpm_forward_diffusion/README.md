# DDPM Forward Diffusion

## 题目
实现 DDPM 前向过程：`x_t = sqrt(alpha_bar_t) x_0 + sqrt(1 - alpha_bar_t) epsilon`。

## 思路
由噪声调度累积 alpha_bar，按时间步 `t` 直接采样 `x_t`。

## 复杂度
- 时间：O(T)
- 空间：O(T)

## 代码
见 [solution.py](solution.py)

