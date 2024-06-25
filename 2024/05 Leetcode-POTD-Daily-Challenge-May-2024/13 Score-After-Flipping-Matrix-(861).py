class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    grid[i][j] = (grid[i][j] + 1) % 2
        columns = [0] * m
        for j in range(m):
            for i in range(n):
                columns[j] += grid[i][j]
        for j in range(m):
            if columns[j] < (n - columns[j]):
               columns[j] = n - columns[j]

        result = 0
        for j in range(m):
            result *= 2
            result += columns[j]

        return result
