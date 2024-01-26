class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        path_cache = [[[0 for ball in range(maxMove + 1)] for ball in range(n)] for ball in range(m)]
        boolean_has_cache = [[[False for ball in range(maxMove + 1)] for ball in range(n)] for ball in range(m)]
        mod = ((10 ** 9) + 7)

        def executePathSearch(i, j, moves):
            if moves > maxMove:
                return 0
            if i >= m or i < 0 or j >= n or j < 0:
                return 1
            if boolean_has_cache[i][j][moves]:
                return path_cache[i][j][moves]
            result = 0
            result = (result + executePathSearch(i + 1, j, moves + 1)) % mod
            result = (result + executePathSearch(i - 1, j, moves + 1)) % mod
            result = (result + executePathSearch(i, j - 1, moves + 1)) % mod
            result = (result + executePathSearch(i, j + 1, moves + 1)) % mod
            path_cache[i][j][moves] = result
            
            boolean_has_cache[i][j][moves] = True
            return result

        return executePathSearch(startRow, startColumn, 0) % mod
