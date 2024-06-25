class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        n = len(grid)
        m = len(grid[0])
        DIRECTIONS = [
            (1, 0),
            (-1, 0),
            (0, -1),
            (0, 1)
        ]

        def isValidIndex(i,j):
            return i >= 0 and i < n and j >= 0 and j < m

        def count(i,j):
            result_here = 0
            for di, dj in DIRECTIONS:
                if not isValidIndex(i+di, j+dj) or grid[i + di][j + dj] == 0:
                    result_here += 1
            return result_here


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    result += count(i, j)
        return result
