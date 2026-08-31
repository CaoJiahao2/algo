from dsa.two_pointers_sliding_window.minimum_window_substring.solution import Solution

def test_min_window():
    assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"

def test_min_window_not_found():
    assert Solution().minWindow("a", "aa") == ""

