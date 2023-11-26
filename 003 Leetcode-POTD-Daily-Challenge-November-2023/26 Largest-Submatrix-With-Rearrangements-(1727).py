class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        results = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 and i > 0:
                    matrix[i][j] += matrix[i - 1][j]

            currentRow = sorted(matrix[i], reverse = True)
            for i in range(n):
                results = max(results, currentRow[i] * (i + 1))

        return results
    