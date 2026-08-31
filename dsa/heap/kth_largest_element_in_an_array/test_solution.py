from dsa.heap.kth_largest_element_in_an_array.solution import Solution

def test_kth_largest():
    assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5

def test_kth_largest_sorted():
    assert Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

