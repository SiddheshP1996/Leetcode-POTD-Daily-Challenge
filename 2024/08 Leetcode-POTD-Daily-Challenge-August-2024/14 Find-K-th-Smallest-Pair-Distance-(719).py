class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        def execute(target):
            count = 0
            right = 0
            for left in range(n):
                while right < n and nums[right] - nums[left] <= target:
                    right += 1
                count += (right - left - 1)
            return count >= k

        left = 0
        right = nums[-1]
        while left < right:
            mid = (left + right) // 2
            if execute(mid):
                right = mid
            else:
                left = mid + 1
        return left
