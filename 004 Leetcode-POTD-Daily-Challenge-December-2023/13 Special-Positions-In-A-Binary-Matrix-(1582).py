class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        rows = [0] * n
        columns = [0] * m

        for i in range(n):
            for j in range(m):
                rows[i] += mat[i][j]
                columns[j] += mat[i][j]
        result = 0
        for i in range(n):
            for j in range(m):
                if rows[i] == 1 and columns[j] == 1 and mat[i][j] == 1:
                    result += 1
        return result
