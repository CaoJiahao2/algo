from dsa.dynamic_programming.coin_change.solution import Solution

def test_coin_change():
    assert Solution().coinChange([1, 2, 5], 11) == 3

def test_coin_change_impossible():
    assert Solution().coinChange([2], 3) == -1

