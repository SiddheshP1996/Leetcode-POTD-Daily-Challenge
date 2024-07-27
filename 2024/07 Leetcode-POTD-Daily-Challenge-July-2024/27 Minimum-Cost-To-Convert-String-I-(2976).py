class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dp = [[float('inf')] * 26 for _ in range(26)]
        
        for i in range(26):
            dp[i][i] = 0
            
        for oldCost, newCost, character in zip(original, changed, cost):
            oldCost, newCost = ord(oldCost) - ord('a'), ord(newCost) - ord('a')
            dp[oldCost][newCost] = min(dp[oldCost][newCost], character)
            
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
                    
        result = sum(dp[ord(string) - ord('a')][ord(trgt) - ord('a')]\
            for string, trgt in zip(source, target))
        
        return result if result != float('inf') else -1
