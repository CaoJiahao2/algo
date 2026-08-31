from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(need)
        left = 0
        start, length = 0, len(s) + 1
        for right, ch in enumerate(s):
            if ch in need:
                need[ch] -= 1
                if need[ch] == 0:
                    missing -= 1
            while missing == 0:
                if right - left + 1 < length:
                    start, length = left, right - left + 1
                left_ch = s[left]
                if left_ch in need:
                    need[left_ch] += 1
                    if need[left_ch] == 1:
                        missing += 1
                left += 1
        return "" if length == len(s) + 1 else s[start:start + length]

