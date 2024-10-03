class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        required = sum(nums) % p
        keyValue = {0: -1}
        current = 0
        result = len(nums)

        for i, array in enumerate(nums):
            current = (current + array) % p
            keyValue[current] = i
            if (current - required) % p in keyValue:
                result = min(result, i - keyValue[(current - required) % p])
        return result if result < len(nums) else -1
