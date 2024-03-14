class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atMost(nums, goal)- self.atMost(nums, goal-1)

    def atMost(self, nums: List[int], goal: int) -> int:
        headPoint, tailPoint, totalCount, result = 0, 0, 0, 0
        for headPoint in range(len(nums)):
            totalCount += nums[headPoint]
            while totalCount > goal and tailPoint <= headPoint:
                totalCount -= nums[tailPoint]
                tailPoint += 1
            result += headPoint - tailPoint + 1
        return result
