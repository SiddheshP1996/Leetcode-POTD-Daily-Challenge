class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        dp = [[[-1] * columns for elements in range(columns)] for elements in range(rows)]
        dp[0][0][columns - 1] = grid[0][0] + grid[0][columns - 1]

        for i in range(1, rows):
            for j in range(columns):
                for k in range(j + 1, columns):
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if 0 <= (j + x) < columns and 0 <= (k + y) < columns:
                                prev = dp[i - 1][j + x][k + y]
                                if prev != -1:
                                    dp[i][j][k] = max(dp[i][j][k], prev + grid[i][j] + (grid[i][k] if j != k else 0))

        result = max(max(row) for row in dp[rows - 1])
        return result if result != -1 else 0
