# KV Cache

## 题目
实现解码时的 KV Cache：缓存历史 key/value，新 token 只与已缓存 KV 计算注意力。

## 思路
维护 K/V 缓存和位置指针，更新时写入当前位置，注意力只读取 `[:pos]` 片段。

## 复杂度
- 时间：单步 O(pos d)
- 空间：O(max_len d)

## 代码
见 [solution.py](solution.py)

