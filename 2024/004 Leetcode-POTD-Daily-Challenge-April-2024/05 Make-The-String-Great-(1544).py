class Solution:
    def makeGood(self, s: str) -> str:
        strArray = []
        for element in range(len(s)):
            if strArray and strArray[-1] == s[element].swapcase():
                strArray.pop()
            else:
                strArray.append(s[element])
        return ''.join(strArray)
