class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        s = [int(c) for c in s]

        def iterateCharacter(previousCharacter, i):
            if i == n:
                return 0
            targetCharacter = (previousCharacter + 1) % 2
            if s[i] == targetCharacter:
                return iterateCharacter(s[i], i + 1)
            return 1 + iterateCharacter(targetCharacter, i + 1)

        return min(iterateCharacter(0, 0), iterateCharacter(1, 0))
