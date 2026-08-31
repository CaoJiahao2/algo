class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos: dict[str, int] = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in pos and pos[ch] >= left:
                left = pos[ch] + 1
            pos[ch] = right
            best = max(best, right - left + 1)
        return best

