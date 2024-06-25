import collections


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        indexes = collections.defaultdict(list)
        n = len(s)
        results = 0
        for i in range(n):
            indexes[s[i]].append(i)
        used = [[False for _ in range(26)] for _ in range(26)]

        for i in range(1, n - 1):
            countOfString = s[i]
            for j in range(26):
                boundaryOfSubsequence = chr(ord('a') + j)
                if used[ord(countOfString) - ord('a')][ord(boundaryOfSubsequence) - ord('a')]:
                    continue
                if boundaryOfSubsequence in indexes:
                    hasLeftIndex = indexes[boundaryOfSubsequence][0] < i
                    hasRightIndex = indexes[boundaryOfSubsequence][-1] > i
                    if hasLeftIndex and hasRightIndex:
                        used[ord(countOfString) - ord('a')][ord(boundaryOfSubsequence) - ord('a')] = True
                        results += 1
        return results
