class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def isValidIndex(i, j):
            return i >= 0 and i < n and j >= 0 and j < m and grid[i][j] == "1"

        def execute(i, j):
            DIRECTIONS = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ]
            for di, dj in DIRECTIONS:
                if isValidIndex(i + di, j + dj):
                    grid[i + di][j + dj] = "2"
                    execute(i + di, j + dj)

        result = 0
        for i in range(n):
            for j in range(m):
                if isValidIndex(i, j):
                    result += 1
                    execute(i, j)
        return result
