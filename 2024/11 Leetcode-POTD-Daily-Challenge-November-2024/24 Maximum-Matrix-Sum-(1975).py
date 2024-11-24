class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        result = multiply = 0
        value = inf 
        for i in range(len(matrix)): 
            for j in range(len(matrix)):
                result += abs(matrix[i][j])
                value = min(value, abs(matrix[i][j]))
                if matrix[i][j] < 0: multiply ^= 1
        return result - 2 * multiply * value
