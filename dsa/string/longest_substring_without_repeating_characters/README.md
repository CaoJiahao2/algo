# Longest Substring Without Repeating Characters

## 题目
给定字符串 `s`，返回不含重复字符的最长子串长度。

## 思路
滑动窗口：右指针扩展，哈希表记录字符最近出现位置；遇到重复则把左指针移到重复字符之后。

## 复杂度
- 时间：O(n)
- 空间：O(min(n, 字符集大小))

## 代码
见 [solution.py](solution.py)

