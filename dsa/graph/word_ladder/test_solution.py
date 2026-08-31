from dsa.graph.word_ladder.solution import Solution

def test_ladder():
    assert Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5

def test_ladder_impossible():
    assert Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0

