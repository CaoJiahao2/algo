from dsa.graph.course_schedule.solution import Solution

def test_can_finish_true():
    assert Solution().canFinish(2, [[1, 0]]) is True

def test_can_finish_false():
    assert Solution().canFinish(2, [[1, 0], [0, 1]]) is False

