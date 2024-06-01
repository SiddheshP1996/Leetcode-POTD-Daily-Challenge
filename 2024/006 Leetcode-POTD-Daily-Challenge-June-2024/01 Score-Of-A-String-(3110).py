class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        def execute(i):
            if i == n:
                return 0
            result = abs(ord(s[i - 1]) - ord(s[i]))
            return result + execute(i + 1)
        return execute(1)
