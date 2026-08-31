# Container With Most Water

## 题目
给定高度数组 `height`，返回两条垂线与 x 轴围成的容器能容纳的最大水量。

## 思路
双指针从两端向中间收敛，每次移动较矮的一侧，记录最大面积。

## 复杂度
- 时间：O(n)
- 空间：O(1)

## 代码
见 [solution.py](solution.py)

