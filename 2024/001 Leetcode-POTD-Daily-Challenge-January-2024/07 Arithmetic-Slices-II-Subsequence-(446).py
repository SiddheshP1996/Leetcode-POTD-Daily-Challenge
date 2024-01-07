class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        totalNumberOfCount = 0
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                difference = nums[i] - nums[j]
                count = dp[j][difference] if difference in dp[j] else 0
                # Add the count to the total and update dp[i][difference]
                totalNumberOfCount += count
                dp[i][difference] += count + 1

        return totalNumberOfCount
