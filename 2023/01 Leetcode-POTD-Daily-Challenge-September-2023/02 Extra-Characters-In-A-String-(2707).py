class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [i for i in range(len(s)+1)]
        dictionary = set(dictionary)
        for i in range(len(s)+1):
            for j in range(i):
                if s[j:i] in dictionary:
                    dp[i] = min(dp[i],dp[j])
                else:
                    dp[i] = min(dp[i],dp[j]+i-j)
        return dp[-1]