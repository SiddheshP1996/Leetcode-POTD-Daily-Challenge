class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp = [float('inf')] * (len(cost) + 1)
        dp[0] = 0
        for i in range(len(cost)):
            for j in range(len(cost), 0, -1): dp[j] = min(dp[j], dp[max(j - time[i] - 1, 0)] + cost[i])
        return dp[len(cost)]
