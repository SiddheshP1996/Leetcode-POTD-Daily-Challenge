class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for number in range(len(nums)):
            if nums[number] != number:
                return number
        return len(nums)
