from dsa.array_hash.two_sum.solution import Solution

def test_two_sum():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_unsorted():
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]

