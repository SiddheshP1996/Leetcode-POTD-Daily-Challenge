class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        dp = {i:1 for i in nums}
        longest = 1
        for i in nums:
            numSquare = i ** 2
            if numSquare in dp:
                dp[numSquare] = dp[i] + 1
                if dp[numSquare] == 5: return dp[numSquare]
                if dp[numSquare] > longest:
                    longest = dp[numSquare]
        return longest if longest != 1 else -1
