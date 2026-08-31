from dsa.string.group_anagrams.solution import Solution

def test_group_anagrams():
    out = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(sorted(g) for g in out) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

