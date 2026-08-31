# 2D Max Pooling（Naive 实现）

## 题目
实现二维最大池化，输入 `(C, H, W)`，支持 kernel_size、stride、padding。

## 思路
在每个池化窗口内取最大值。

## 复杂度
- 时间：O(C * H_out * W_out * KH * KW)
- 空间：O(C * H_out * W_out)

## 代码
见 [solution.py](solution.py)
