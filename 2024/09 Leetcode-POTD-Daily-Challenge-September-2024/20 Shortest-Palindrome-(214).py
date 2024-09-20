class Solution:
    def shortestPalindrome(self, s: str) -> str:
        result = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(result[i:]):
                return result[:i] + s
