from dsa.heap.top_k_frequent_elements.solution import Solution

def test_top_k_frequent():
    assert sorted(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]

