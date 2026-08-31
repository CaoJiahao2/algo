from dsa.binary_search_sort.search_in_rotated_sorted_array.solution import Solution

def test_rotated_found():
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4

def test_rotated_not_found():
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 3) == -1

