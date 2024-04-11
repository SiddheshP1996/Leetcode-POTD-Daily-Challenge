class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        result = []
        n = len(num)
        if k >= n:
            return "0"
        finalLength = n - k
        for i in range(n):
            digit = int(num[i])
            while len(result) > 0 and digit < result[-1] and ((n - (i + 1)) + len(result)) >= finalLength:
                result.pop()
            result.append(digit)
        while len(result) > finalLength:
            result.pop()

        resultString = "".join(str(d) for d in result)
        left = 0
        while left < (len(resultString) - 1) and resultString[left] == "0":
            left += 1
        return resultString[left::]
