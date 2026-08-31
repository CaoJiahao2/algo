from dsa.stack_queue.daily_temperatures.solution import Solution

def test_daily_temperatures():
    assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]

def test_daily_temperatures_decreasing():
    assert Solution().dailyTemperatures([30, 20, 10]) == [0, 0, 0]

