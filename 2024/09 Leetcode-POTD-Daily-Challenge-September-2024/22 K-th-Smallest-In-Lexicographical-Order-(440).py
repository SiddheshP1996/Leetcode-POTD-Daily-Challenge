class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def prefixCount(prefix, n):
            count = 0
            currentPrefix = prefix
            nextPrefix = prefix + 1
            while currentPrefix <= n:
                count += min(nextPrefix, n + 1) - currentPrefix
                currentPrefix *= 10
                nextPrefix *= 10
            return count
        
        currentCount = 1
        k -= 1
        
        while k > 0:
            count = prefixCount(currentCount, n)
            if k >= count:
                k -= count
                currentCount += 1
            else:
                currentCount *= 10
                k -= 1
        
        return currentCount
