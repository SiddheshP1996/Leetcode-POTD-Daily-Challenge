class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        dp1, dp2 = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: dp1[i] = max(dp1[i], 1 + dp1[j])
                if nums[j] > nums[i]: 
                    if dp1[j] > 1: dp2[i] = max(dp2[i], 1 + dp1[j])
                    if dp2[j] > 1: dp2[i] = max(dp2[i], 1 + dp2[j])
        
        return len(nums) - max(dp2)
