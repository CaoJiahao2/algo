class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i: int, j: int) -> None:
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(i + di, j + dj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count

