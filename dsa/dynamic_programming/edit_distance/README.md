# Edit Distance

## 题目
给定两个单词，返回将 `word1` 转换为 `word2` 所需的最少操作数（插入、删除、替换）。

## 思路
二维 DP：字符相同时取对角线，否则取三种操作的最小值加一。

## 复杂度
- 时间：O(m n)
- 空间：O(m n)

## 代码
见 [solution.py](solution.py)

