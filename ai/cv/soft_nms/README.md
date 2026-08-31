# Soft NMS

## 题目
用 Soft NMS 对候选框去重：对高重叠框不做硬删除，而是按 IoU 对其得分做衰减。

## 思路
与 NMS 相同地按得分遍历；每次选中最高分框后，对剩余框执行高斯衰减
`s *= exp(-iou^2 / sigma)`，低于 `score_threshold` 的框被丢弃。

## 复杂度
- 时间：O(K*N)
- 空间：O(N)

## 代码
见 [solution.py](solution.py)
