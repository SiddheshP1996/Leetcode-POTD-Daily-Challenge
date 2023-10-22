class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [-float('inf')] * (len(nums2) + 1)

        for i in range(1, len(nums1) + 1):
            temp = [-float('inf')] * (len(nums2) + 1)
            for j in range(1, len(nums2) + 1):
                cur = nums1[i - 1] * nums2[j - 1]
                temp[j] = max([cur, cur + dp[j - 1], dp[j], temp[j - 1]])
            dp = temp
        return temp[-1]
