# NMS（Non-Maximum Suppression）

## 题目
给定候选框和得分，返回非极大值抑制后保留下来的框索引。

## 思路
按得分降序遍历；当前最高分框一定保留，并抑制所有与其 IoU 超过阈值的其余框。

## 复杂度
- 时间：O(K*N)，K 为保留框数
- 空间：O(N)

## 代码
见 [solution.py](solution.py)
