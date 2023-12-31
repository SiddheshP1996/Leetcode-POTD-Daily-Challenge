class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = ((10 ** 9) + 7)

        cache = [[0 for _ in range(5)] for _ in range(n + 1)]
        hasCache = [[False for _ in range(5)] for _ in range(n + 1)]
        idxMap = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        def go(c, k):
            if k == n:
                return 1
            if hasCache[k][idxMap[c]]:
                return cache[k][idxMap[c]]
            result = 0
            if c == 'a':
                result = 1 * go('e', k + 1)
            if c == 'e':
                result = (1 * go('a', k + 1)) + (1 * go('i', k + 1))
            if c == 'i':
                result = (1 * go('a', k + 1)) + \
                      (1 * go('e', k + 1)) + \
                      (1 * go('o', k + 1)) + \
                      (1 * go('u', k + 1))
            if c == 'o':
                result = (1 * go('i', k + 1)) + (1 * go('u', k + 1))
            if c == 'u':
                result = 1 * go('a', k + 1)
            hasCache[k][idxMap[c]] = True
            cache[k][idxMap[c]] = result
            return result

        result = 0
        letters = ['a', 'e', 'i', 'o', 'u']
        for c in letters:
            result += (1 * go(c, 1)) % mod
        return result % mod
    