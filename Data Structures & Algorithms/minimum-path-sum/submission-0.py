class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}
        def f(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            if r < 0 or c < 0 or r >= m or c >= n:
                return float('inf')
            if r == m - 1 and c == n - 1:
                return grid[r][c]
            result = grid[r][c] + min(f(r, c + 1), f(r + 1, c))
            memo[(r,c)] = result
            return result
        return f(0,0)