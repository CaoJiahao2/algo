# Climbing Stairs

## 题目
每次可爬 1 或 2 阶，返回爬到第 `n` 阶的方法数。

## 思路
动态规划：`dp[i] = dp[i-1] + dp[i-2]`，可滚动变量优化空间。

## 复杂度
- 时间：O(n)
- 空间：O(1)

## 代码
见 [solution.py](solution.py)

