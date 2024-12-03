class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        i = len(s) - 1
        while i >= 0:
            result.append(s[i])
            if spaces and i == spaces[-1]:
                result.append(' ')
                spaces.pop()
            i -= 1    
        return ''.join(result[:: -1])
