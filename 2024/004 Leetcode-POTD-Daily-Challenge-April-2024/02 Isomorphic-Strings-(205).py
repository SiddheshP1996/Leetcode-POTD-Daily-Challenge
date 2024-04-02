class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        zipSet = set(zip(s, t))
        return len(zipSet) == len(set(s)) == len(set(t))
