class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ratingLength = len(rating)
        dp = [[[0] * 2 for _ in range(3)] for _ in range(ratingLength)]
        
        for element in range(ratingLength):
            dp[element][0][0] = dp[element][0][1] = 1
        
        for element in range(ratingLength):
            for need in range(1, 3):
                for j in range(element):
                    if rating[element] > rating[j]:
                        dp[element][need][0] += dp[j][need - 1][0]
                    if rating[element] < rating[j]:
                        dp[element][need][1] += dp[j][need - 1][1]
        
        result = 0
        for element in range(ratingLength):
            result += dp[element][2][0] + dp[element][2][1]
        
        return result
