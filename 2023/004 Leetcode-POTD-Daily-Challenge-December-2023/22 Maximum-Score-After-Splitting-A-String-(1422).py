class Solution:
    def maxScore(self, s: str) -> int:
        result = 0
        n = len(s)
        allZeros = [0] * n
        allZeros[0] = 1 if s[0] == "0" else 0
        for i in range(1, n):
            allZeros[i] = allZeros[i - 1] + (1 if s[i] == "0" else 0)

        allOnes = 0
        for i in range(n - 1):
            if s[i] == "1":
                allOnes += 1
            oneAtRight = (n - allZeros[-1] - allOnes)
            resultHere = allZeros[i] + oneAtRight
            result = max(resultHere, result)
        return result
