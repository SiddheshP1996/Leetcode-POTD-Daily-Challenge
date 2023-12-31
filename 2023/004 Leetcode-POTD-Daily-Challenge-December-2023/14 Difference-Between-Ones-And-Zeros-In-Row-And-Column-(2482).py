class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        onesInRows = [0] * n
        onesInColumns = [0] * m
        result = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                onesInRows[i] += grid[i][j]
                onesInColumns[j] += grid[i][j]

        for i in range(n):
            for j in range(m):
                zerosInRows = n - onesInRows[i]
                zerosInColumns = m - onesInColumns[j]
                result[i][j] = onesInRows[i] + onesInColumns[j] - zerosInRows - zerosInColumns
        return result
