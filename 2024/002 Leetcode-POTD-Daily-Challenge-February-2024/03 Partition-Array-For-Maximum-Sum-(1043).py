class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n
        
        # Handle the first k indexes differently
        for numbers in range(k): dp[numbers] = max(arr[:numbers + 1]) * (numbers + 1)
        
        # We can get rid of index i by running i times
        for numbers in range(k, n):
            current_list = []
            for max_sum in range(k):
                current_list.append(dp[numbers - max_sum - 1] + max(arr[(numbers - max_sum):(numbers + 1)]) * (max_sum + 1))
            dp[numbers] = max(current_list)

        return dp[-1]
