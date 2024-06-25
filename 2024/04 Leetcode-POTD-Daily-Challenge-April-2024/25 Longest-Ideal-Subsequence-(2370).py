class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        cache = [[0 for _ in range(26)] for _ in range(n)]
        hasCache = [[False for _ in range(26)] for _ in range(n)]

        def execute(previous, i):
            if i == n:
                return 0
            if hasCache[i][previous]:
                return cache[i][previous]
            current = ord(s[i]) - ord('a')
            result = 0
            if abs(current - previous) <= k:
                result = max(result, 1 + execute(current, i + 1))
            result = max(result, execute(previous, i + 1))
            hasCache[i][previous] = True
            cache[i][previous] = result
            return result

        result = 0
        for i in range(n):
            result = max(result, execute(ord(s[i]) - ord('a'), i))
        return result
