class Solution:
    def dfs(self, arrLen, index, steps, csteps, dp):
        mod = ((10 ** 9) + 7)
        # base cases
        if index == 0 and csteps == steps:
            return 1
        elif csteps == steps:
            return 0
        key = (index, csteps)
        if key in dp:
            return dp[key]
        score = 0
        # can either stay
        score = self.dfs(arrLen, index, steps, csteps + 1, dp)
        # can move left..
        if index > 0:
            score += self.dfs(arrLen, index - 1, steps, csteps + 1, dp)
        # can move right..
        if index < arrLen - 1:
            score += self.dfs(arrLen, index + 1, steps, csteps + 1, dp)
        dp[key] = score % mod
        return dp[key]

    def numWays(self, steps: int, arrLen: int) -> int:
        return self.dfs(arrLen, 0, steps, 0, {})
