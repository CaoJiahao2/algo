# Word Ladder

## 题目
给定起始词 `beginWord`、目标词 `endWord` 和词典 `wordList`，每次只能改一个字母且中间词必须在词典中，返回最短变换序列长度；无法到达则返回 0。

## 思路
BFS + 通配符模式建图：把每个词替换一位为 `*` 作为中间节点，分层搜索最短路径。

## 复杂度
- 时间：O(n L^2)
- 空间：O(n L)

## 代码
见 [solution.py](solution.py)

