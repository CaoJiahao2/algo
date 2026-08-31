from dsa.backtracking.permutations.solution import Solution

def test_permute():
    assert Solution().permute([1, 2, 3]) == [
        [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
    ]

