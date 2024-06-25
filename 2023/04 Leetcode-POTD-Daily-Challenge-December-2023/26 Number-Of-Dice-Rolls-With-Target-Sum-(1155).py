class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7

        cacheData = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        hasTheCacheData = [[False for _ in range(target + 1)] for _ in range(n + 1)]

        def findNumberOfDiceRolled(i, target):
            if (target > i * k) or target <= 0:
                return 0
            if i == 1:
                if target > k:
                    return 0
                return 1
            if hasTheCacheData[i][target]:
                return cacheData[i][target]
            result = 0
            for j in range(k, 0, -1):
                result = (result + findNumberOfDiceRolled(i - 1, target - j)) % mod
            cacheData[i][target] = result
            hasTheCacheData[i][target] = True
            return result

        return findNumberOfDiceRolled(n, target)
