from dsa.dynamic_programming.longest_increasing_subsequence.solution import Solution

def test_lis():
    assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4

def test_lis_single():
    assert Solution().lengthOfLIS([7, 7, 7, 7]) == 1

