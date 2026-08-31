from dsa.array_hash.longest_consecutive_sequence.solution import Solution

def test_longest_consecutive():
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4

def test_longest_consecutive_empty():
    assert Solution().longestConsecutive([]) == 0

