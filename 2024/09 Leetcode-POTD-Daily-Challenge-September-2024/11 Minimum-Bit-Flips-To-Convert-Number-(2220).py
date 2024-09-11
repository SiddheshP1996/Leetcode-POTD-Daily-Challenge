class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xorResult = start ^ goal
        return bin(xorResult).count('1')
