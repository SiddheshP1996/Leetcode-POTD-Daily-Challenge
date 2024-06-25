class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        start = 0
        end = 0
        totalsum = sum(nums)
        sum_to_make = totalsum - x
        if totalsum == x:
            return len(nums)
        ans = 0
        summ = 0
        while end < len(nums):
            summ += nums[end]
            while start < end and summ > sum_to_make:
                summ -= nums[start]
                start += 1
            if summ == sum_to_make:
                ans = max(ans, end - start + 1)
            end += 1
        return -1 if ans == 0 else len(nums) - ans