class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        start = 0
        result = []
        for i in range(n):
            row = []
            for j in range(m):
                if i + 2 >= n or j + 2 >= m:
                    continue
                maximumLocal = -1
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        maximumLocal = max(maximumLocal, grid[k][l])
                row.append(maximumLocal)
            if len(row) > 0:
                result.append(row)

        return result
