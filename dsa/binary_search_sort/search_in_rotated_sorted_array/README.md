# Search in Rotated Sorted Array

## 题目
给定旋转后的升序数组（无重复元素）和目标值，返回下标；不存在返回 -1。

## 思路
二分时判断哪一侧有序，再决定目标是否落在有序侧并收缩区间。

## 复杂度
- 时间：O(log n)
- 空间：O(1)

## 代码
见 [solution.py](solution.py)

