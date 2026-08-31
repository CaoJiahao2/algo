from dsa.two_pointers_sliding_window.container_with_most_water.solution import Solution

def test_max_area():
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

def test_max_area_two():
    assert Solution().maxArea([1, 1]) == 1

