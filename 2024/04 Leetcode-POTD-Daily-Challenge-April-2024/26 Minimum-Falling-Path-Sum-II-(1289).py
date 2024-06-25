class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        inf = 10 ** 20
        cache = list(grid[0])
        for i in range(1, n):
            minimumSeen = inf
            row = list(grid[i])
            for j in range(m):
                grid[i][j] = row[j] + minimumSeen
                minimumSeen = min(minimumSeen, cache[j])
            minimumSeen = inf
            for j in range(m - 1, -1, -1):
                grid[i][j] = min(row[j] + minimumSeen, grid[i][j])
                minimumSeen = min(minimumSeen, cache[j])
            cache = list(grid[i])
        return min(grid[-1])
