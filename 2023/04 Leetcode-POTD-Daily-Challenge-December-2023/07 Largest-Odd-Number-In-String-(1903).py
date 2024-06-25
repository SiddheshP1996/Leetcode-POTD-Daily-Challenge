class Solution:
    def largestOddNumber(self, num: str) -> str:
        for oddNumber in range(len(num) -1,-1,-1):
            if int(num[oddNumber]) % 2 == 1:
                return num[0:oddNumber + 1]
        return ""
