from collections import Counter

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        arrayCount = Counter()
        arrayCount[0] += 1
        currentCount = 0
        n = len(nums)
        result = 0
        for i in range(n):
            currentCount += nums[i]
            currentCount %= k
            if currentCount in arrayCount:
                result += arrayCount[currentCount]
            arrayCount[currentCount] += 1
        return result
