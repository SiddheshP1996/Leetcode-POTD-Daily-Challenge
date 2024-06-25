class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        result = 1
        for i in range(n):
            while nums[i] > 0 and nums[i] < n and (nums[i] - 1) != i:
                if  nums[(nums[i] - 1)] == nums[i]:
                    break
                temp = nums[(nums[i] - 1)]
                nums[(nums[i] - 1)] = nums[i]
                nums[i] = temp
        for i in range(n):
            if nums[i] == result:
                result += 1
        return result