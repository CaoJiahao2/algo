# Coin Change

## 题目
给定硬币面额数组和目标金额，返回凑成该金额所需的最少硬币数；无法凑成返回 -1。

## 思路
完全背包 DP：`dp[x] = min(dp[x], dp[x - coin] + 1)`。

## 复杂度
- 时间：O(amount * n)
- 空间：O(amount)

## 代码
见 [solution.py](solution.py)

