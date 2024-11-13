class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)-1, -1, -1):
            value = nums[i]
            lineA = bisect_left(nums, lower - value, lo = 0, hi = i)
            lineB = bisect_right(nums, upper - value, lo = 0, hi = i)
            result += lineB - lineA
        return result
