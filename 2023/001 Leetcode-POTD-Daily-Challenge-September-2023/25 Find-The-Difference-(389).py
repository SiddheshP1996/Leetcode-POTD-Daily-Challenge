class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """Here "i" is referred to as elements"""
        for i in t:
            if i not in s:
                return i
            elif t.count(i) != s.count(i):
                return i
