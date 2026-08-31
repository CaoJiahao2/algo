from dsa.backtracking.subsets.solution import Solution

def test_subsets():
    out = Solution().subsets([1, 2, 3])
    assert sorted(out) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

