# IoU（Intersection over Union）

## 题目
计算两组边界框之间的 IoU。边界框格式为 `[x1, y1, x2, y2]`（左上、右下坐标）。

## 思路
先取两框交集左上/右下坐标，`clamp(min=0)` 得到交面积；并集 = 面积和 - 交集。支持 `(N,4)` 与 `(M,4)` 广播，返回 `(N,M)`。

## 复杂度
- 时间：O(N*M)
- 空间：O(N*M)

## 代码
见 [solution.py](solution.py)
