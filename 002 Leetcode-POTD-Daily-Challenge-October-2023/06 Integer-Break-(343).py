class Solution:
    def integerBreak(self, n: int) -> int:
        """
        True Dynamic Programming Solution
        """
        dp = {1: 1}

        for num in range(2, n + 1):
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                value = dp[i] * dp[num - i]
                dp[num] = max(dp[num], value)
        return dp[n]


"""
Recursive Solution Time Complexity O(n^2) Space Complexity is O(n)
        # dp = {1: 1}
        def dfs(num):
            if num in dp:
                return dp[num]

            dp[num] = 0 if num == n else num
            for i in range(1, num):
                value = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num], value)
            return dp[num]

        return dfs(n)
"""
