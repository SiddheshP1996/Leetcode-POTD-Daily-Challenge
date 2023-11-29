class Solution:
    def hammingWeight(self, n: int) -> int:
        results = 0
        while n > 0:
            if n % 2 != 0:
                results += 1
            n = (n >> 1)
        return results
    