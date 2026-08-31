# 2D 卷积（Naive 实现）

## 题目
实现朴素二维卷积，输入 `(C_in, H, W)`，卷积核 `(C_out, C_in, KH, KW)`，支持 stride 和 padding。

## 思路
先 pad 输入，再对每个输出位置取感受野与对应输出通道卷积核逐元素乘加。

## 复杂度
- 时间：O(C_out * C_in * KH * KW * H_out * W_out)
- 空间：O(C_out * H_out * W_out)

## 代码
见 [solution.py](solution.py)
