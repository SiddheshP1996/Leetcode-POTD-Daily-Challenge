class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        pointerOne, pointerTwo = 0, 0

        while pointerOne < len(str1) and pointerTwo < len(str2):
            if (ord(str2[pointerTwo]) - ord(str1[pointerOne]) + 26) % 26 <= 1:
                pointerTwo += 1
            pointerOne += 1

        return pointerTwo == len(str2)
