class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(m, n):
            if m < 0 or m >= rows or n < 0 or n >= cols or grid[m][n] == '0':
                return
            grid[m][n] = '0'
            dfs(m + 1, n)
            dfs(m, n + 1)
            dfs(m - 1, n)
            dfs(m, n - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)

        return num_islands