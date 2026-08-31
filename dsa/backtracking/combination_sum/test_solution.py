from dsa.backtracking.combination_sum.solution import Solution

def test_combination_sum():
    out = Solution().combinationSum([2, 3, 6, 7], 7)
    assert sorted(sorted(c) for c in out) == [[2, 2, 3], [7]]

