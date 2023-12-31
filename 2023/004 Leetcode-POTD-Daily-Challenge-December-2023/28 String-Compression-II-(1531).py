class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[9999] * 110 for character in range(110)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(0, k + 1):
                countCharacter, deleteCharacter = 0, 0
                for l in range(i, 0, -1):
                    if s[l - 1] == s[i - 1]:
                        countCharacter += 1
                    else:
                        deleteCharacter += 1

                    if j - deleteCharacter >= 0:
                        dp[i][j] = min(dp[i][j], dp[l - 1][j - deleteCharacter] + 1 + (3 if countCharacter >= 100 else 2 if countCharacter >= 10 else 1 if countCharacter >= 2 else 0))

                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

        return dp[n][k]
