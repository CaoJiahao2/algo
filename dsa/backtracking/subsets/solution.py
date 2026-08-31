class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        def backtrack(start: int, path: list[int]) -> None:
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return res

