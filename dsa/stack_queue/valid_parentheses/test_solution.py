from dsa.stack_queue.valid_parentheses.solution import Solution

def test_valid():
    assert Solution().isValid("()[]{}") is True

def test_invalid():
    assert Solution().isValid("(]") is False

