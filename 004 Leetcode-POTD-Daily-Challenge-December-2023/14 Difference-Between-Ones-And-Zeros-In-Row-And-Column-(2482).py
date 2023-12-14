class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        onesKeRows = [0] * n
        onesKeColumns = [0] * m
        result = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                onesKeRows[i] += grid[i][j]
                onesKeColumns[j] += grid[i][j]

        for i in range(n):
            for j in range(m):
                zerosKeRows = n - onesKeRows[i]
                zerosKeColumns = m - onesKeColumns[j]
                result[i][j] = onesKeRows[i] + onesKeColumns[j] - zerosKeRows - zerosKeColumns
        return result
