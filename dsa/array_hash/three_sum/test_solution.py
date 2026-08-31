from dsa.array_hash.three_sum.solution import Solution

def test_three_sum():
    out = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    assert sorted(sorted(t) for t in out) == [[-1, -1, 2], [-1, 0, 1]]

def test_three_sum_empty():
    assert Solution().threeSum([0, 1, 1]) == []

