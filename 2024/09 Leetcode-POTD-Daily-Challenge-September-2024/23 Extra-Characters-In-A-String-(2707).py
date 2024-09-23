class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        maxValue = len(s) + 1
        dp = [maxValue] * (len(s) + 1)
        dp[0] = 0 
        dictionarySet = set(dictionary)

        for element in range(1, len(s) + 1):
            dp[element] = dp[element - 1] + 1

            for elementList in range(1, element + 1): 
                if s[element - elementList:element] in dictionarySet:
                    dp[element] = min(dp[element], dp[element - elementList])
                    
        return dp[-1]
