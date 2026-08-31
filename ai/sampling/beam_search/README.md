# Beam Search

## 题目
实现 Beam Search 解码：每步保留累计对数概率最高的 `beam_width` 条路径。

## 思路
维护候选路径集合，每步扩展 top-k token，按累计分数截断，遇到 EOS 可提前结束。

## 复杂度
- 时间：O(max_len * beam * V)
- 空间：O(beam * max_len)

## 代码
见 [solution.py](solution.py)

