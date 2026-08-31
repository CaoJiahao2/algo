# Course Schedule

## 题目
给定课程数 `numCourses` 和先修关系 `prerequisites`（`[a, b]` 表示先修 b 再修 a），判断能否完成所有课程（即图无环）。

## 思路
拓扑排序（Kahn 算法）：统计入度，不断移除入度为 0 的节点；若访问完所有节点则无环。

## 复杂度
- 时间：O(V + E)
- 空间：O(V + E)

## 代码
见 [solution.py](solution.py)

