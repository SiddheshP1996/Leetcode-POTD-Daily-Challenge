class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffixProduct = list(nums)
        prefixProduct = list(nums)
        n = len(nums)
        for i in range(1, n):
            prefixProduct[i] = prefixProduct[i - 1] * nums[i]
        for i in range(n - 2, -1, -1):
            suffixProduct[i] = suffixProduct[i + 1] * nums[i]

        result = [1] * n
        for i in range(n):
            preffixx = prefixProduct[i - 1] if i > 0 else 1
            suffixx = suffixProduct[i + 1] if i < n - 1 else 1
            result[i] = preffixx * suffixx
        return result
