class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        nums.sort()
        lenOfNums = len(nums)
        previousSum = [0] * lenOfNums
        previousSum[0] = nums[0]
        for allNum in range(1, lenOfNums):
            previousSum[allNum] = previousSum[allNum - 1] + nums[allNum]
        result = -1
        for allNum in range(2, lenOfNums):
            if previousSum[allNum - 1] > nums[allNum]:
                result = previousSum[allNum]
        return result
