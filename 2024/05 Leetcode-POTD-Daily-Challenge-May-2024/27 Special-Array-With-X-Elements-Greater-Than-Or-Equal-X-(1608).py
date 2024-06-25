from bisect import bisect_left

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for x in range(1, n + 1):
            count = bisect_left(nums, x)
            if (n - count) == x:
                return x
        return -1
