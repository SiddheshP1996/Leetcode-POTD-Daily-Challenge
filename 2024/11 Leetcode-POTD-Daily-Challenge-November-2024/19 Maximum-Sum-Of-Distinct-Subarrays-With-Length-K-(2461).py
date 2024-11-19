class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        count = defaultdict(int)
        curSum = 0

        left = 0
        for right in range(len(nums)):
            curSum += nums[right]
            count[nums[right]] += 1

            if right - left + 1 > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    count.pop(nums[left])
                curSum -= nums[left]
                left += 1

            if len(count) == right - left + 1 == k:
                result = max(result, curSum)

        return result
