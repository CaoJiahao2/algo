from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        cnt = Counter(nums)
        return [x for x, _ in heapq.nlargest(k, cnt.items(), key=lambda item: item[1])]

