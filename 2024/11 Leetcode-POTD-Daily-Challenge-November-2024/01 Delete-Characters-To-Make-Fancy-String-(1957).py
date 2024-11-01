class Solution:
    def makeFancyString(self, s: str) -> str:
        result = s[0]
        count = 1
        for i in range(1, len(s)):
            if s[i] == result[-1]:
                count += 1
                if count < 3:
                    result += s[i]
            else:
                count = 1
                result += s[i]
        return result
