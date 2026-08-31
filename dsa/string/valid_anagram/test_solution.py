from dsa.string.valid_anagram.solution import Solution

def test_anagram_true():
    assert Solution().isAnagram("anagram", "nagaram") is True

def test_anagram_false():
    assert Solution().isAnagram("rat", "car") is False

