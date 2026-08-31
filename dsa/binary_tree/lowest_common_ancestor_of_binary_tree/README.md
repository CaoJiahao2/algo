# Lowest Common Ancestor of Binary Tree

## 题目
给定二叉树和两个节点 `p`、`q`，返回它们的最近公共祖先。

## 思路
递归：若当前节点为 p 或 q 或空则返回；若左右子树各找到一个，则当前节点即 LCA。

## 复杂度
- 时间：O(n)
- 空间：O(n)

## 代码
见 [solution.py](solution.py)

