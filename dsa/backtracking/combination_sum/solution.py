class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res: list[list[int]] = []
        def backtrack(start: int, path: list[int], remaining: int) -> None:
            if remaining == 0:
                res.append(path[:])
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])
                path.pop()
        backtrack(0, [], target)
        return res

