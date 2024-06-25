class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        INF = 10 ** 20
        n = len(nums)
        hasCache = [False] * n
        cache = [INF] * n

        def completeExecution(i):
            if i == n:
                return 0
            if i > n:
                return INF
            if hasCache[i]:
                return cache[i]
            result = INF
            if i + 1 < n and nums[i + 1] == nums[i]:
                result = min(result, 1 + completeExecution(i + 2))
                if i + 2 < n and nums[i + 2] == nums[i]:
                    result = min(result, 1 + completeExecution(i + 3))
            cache[i] = result
            hasCache[i] = True
            return result
        result = completeExecution(0)
        if result >= INF:
            return -1
        return result
