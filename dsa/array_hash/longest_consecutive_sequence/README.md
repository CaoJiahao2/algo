# Longest Consecutive Sequence

## 题目
给定未排序整数数组，返回最长连续元素序列的长度。要求 O(n) 时间。

## 思路
将所有数放入集合；对每个数，若其前驱不在集合中，则作为序列起点向后延伸，更新最大值。

## 复杂度
- 时间：O(n)
- 空间：O(n)

## 代码
见 [solution.py](solution.py)

