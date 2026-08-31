# Top K Frequent Elements

## 题目
给定整数数组和整数 `k`，返回出现频率最高的 `k` 个元素。

## 思路
统计频次后用堆取出频次最高的 `k` 个；或使用快速选择/桶排序。

## 复杂度
- 时间：O(n log k)
- 空间：O(n)

## 代码
见 [solution.py](solution.py)

