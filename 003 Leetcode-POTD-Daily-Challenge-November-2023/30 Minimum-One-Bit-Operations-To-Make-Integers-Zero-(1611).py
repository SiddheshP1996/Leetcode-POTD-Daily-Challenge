class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        results = 0
        while n:
            results = -results - (n ^ (n - 1))
            n &= n - 1
        return abs(results)
