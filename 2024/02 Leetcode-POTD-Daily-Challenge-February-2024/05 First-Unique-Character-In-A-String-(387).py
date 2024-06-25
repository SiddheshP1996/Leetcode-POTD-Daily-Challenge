class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for item in range(len(s)):
            if count[s[item]] == 1:
                return item
        return -1
