from collections import Counter

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = Counter([0])
        maxOR = 0
        for num in nums:
            for val, count in list(dp.items()):
                dp[val | num] += count
            maxOR |= num

        return dp[maxOR]
