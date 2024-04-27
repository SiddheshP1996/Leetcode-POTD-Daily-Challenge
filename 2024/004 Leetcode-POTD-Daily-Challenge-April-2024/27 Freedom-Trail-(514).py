class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)
        inf = float('inf')
        has_cache = [[False for _ in range(m)] for _ in range(n)]
        cache = [[inf for _ in range(m)] for _ in range(n)]

        def execute(i, j):
            if j == m:
                return 0
            if has_cache[i][j]:
                return cache[i][j]
            has_cache[i][j] = True
            result = inf
            for k in range(n):
                if ring[(i + k) % n] == key[j] or ring[(i - k) % n] == key[j]:
                    nextPosition = (i + k) % n if ring[(i + k) % n] == key[j] else (i - k) % n
                    distance = min(k, n - k) + 1
                    subResult = execute(nextPosition, j + 1)
                    result = min(result, distance + subResult)
            cache[i][j] = result
            return result

        return execute(0, 0)
