from dsa.dynamic_programming.edit_distance.solution import Solution

def test_edit_distance():
    assert Solution().minDistance("horse", "ros") == 3

def test_edit_distance_equal():
    assert Solution().minDistance("abc", "abc") == 0

