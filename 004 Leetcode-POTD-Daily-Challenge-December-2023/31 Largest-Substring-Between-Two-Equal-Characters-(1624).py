class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        lastSeen = [n] * 26
        result = -1

        for i in range(n):
            ch = s[i]
            c = ord(ch) - ord('a')
            resultHere = (i - lastSeen[c] - 1)
            result = max(resultHere, result)
            lastSeen[c] = min(i, lastSeen[c])
        return result
