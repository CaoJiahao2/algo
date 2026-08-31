# Kth Largest Element in an Array

## 题目
给定整数数组和整数 `k`，返回数组中第 `k` 大的元素。

## 思路
快速选择：按枢轴分区，递归定位第 `len(nums) - k` 小的元素。

## 复杂度
- 时间：平均 O(n)
- 空间：O(1)

## 代码
见 [solution.py](solution.py)

