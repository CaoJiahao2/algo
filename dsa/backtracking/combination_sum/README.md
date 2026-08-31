# Combination Sum

## 题目
给定候选数组 `candidates`（无重复元素）和目标值 `target`，返回所有和为 `target` 的组合，同一数字可重复使用。

## 思路
回溯：从起始下标枚举，剩余值减当前数字，等于 0 时收集路径。

## 复杂度
- 时间：O(2^target 量级)
- 空间：O(target / min(candidates))

## 代码
见 [solution.py](solution.py)

