class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        results = (-(10**20))
        n = len(nums)
        leftPart = 0
        rightPart = n - 1
        while leftPart < rightPart:
            results = max(results,nums[leftPart] + nums[rightPart])
            leftPart += 1
            rightPart -= 1
        return results
