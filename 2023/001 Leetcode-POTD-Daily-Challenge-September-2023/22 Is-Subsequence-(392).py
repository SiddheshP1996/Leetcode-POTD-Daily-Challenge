class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length1 = len(s)
        length2 = len(t)
        i, j = 0, 0
        while i < length1 and j < length2:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == length1
    