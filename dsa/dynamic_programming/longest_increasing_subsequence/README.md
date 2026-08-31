# Longest Increasing Subsequence

## 题目
给定整数数组，返回最长严格递增子序列的长度。

## 思路
耐心排序：维护一个递增的 `tails`，对每个数二分定位插入位置；`tails` 长度即答案。

## 复杂度
- 时间：O(n log n)
- 空间：O(n)

## 代码
见 [solution.py](solution.py)

