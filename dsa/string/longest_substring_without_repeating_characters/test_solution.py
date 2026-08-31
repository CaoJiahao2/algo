from dsa.string.longest_substring_without_repeating_characters.solution import Solution

def test_longest_substring():
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3

def test_longest_substring_single():
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1

