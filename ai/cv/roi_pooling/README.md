# RoI Pooling

## 题目
给定特征图和若干 RoI（`[x1, y1, x2, y2]`），将每个 RoI 分成 `out_h x out_w` 个 bin，每个 bin 内做最大池化。

## 思路
对每个 RoI 的每个 bin 计算整数像素区间，取出对应区域并取最大值。

## 复杂度
- 时间：O(N * C * out_h * out_w * bin_area)
- 空间：O(N * C * out_h * out_w)

## 代码
见 [solution.py](solution.py)
