class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        result = 0
        n = len(grid)
        m = len(grid[0])

        def isValidIndex(i, j):
            return i >= 0 and i < n and j >= 0 and j < m and grid[i][j] > 0

        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        def getGold(i, j):
            resultHere = grid[i][j]
            grid[i][j] = 0
            bestPath = 0
            for directionY, directionX in DIRECTIONS:
                if isValidIndex(i + directionY, j + directionX):
                    bestPath = max(bestPath, getGold(i + directionY, j + directionX))
            grid[i][j] = resultHere
            resultHere += bestPath
            return resultHere

        for i in range(n):
            for j in range(m):
                if isValidIndex(i, j):
                    result = max(result, getGold(i, j))

        return result
