class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack: list[str] = []
        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            else:
                if not stack or stack.pop() != pairs[ch]:
                    return False
        return not stack

