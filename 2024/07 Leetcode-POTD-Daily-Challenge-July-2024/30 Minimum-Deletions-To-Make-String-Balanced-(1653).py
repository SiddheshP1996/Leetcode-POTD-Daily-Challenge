class Solution:
    def minimumDeletions(self, s: str) -> int:
        stringLength = len(s)
        countOfA = [0] * stringLength
        countOfB = [0] * stringLength
        
        countOfA[-1] = 1 if s[-1] == 'a' else 0
        countOfB[0] = 1 if s[0] == 'b' else 0
        
        for indexItem in range(1, stringLength):
            countOfB[indexItem] = countOfB[indexItem - 1]
            if s[indexItem] == 'b':
                countOfB[indexItem] += 1
                
        for indexItem in range(stringLength - 2, -1, -1):
            countOfA[indexItem] = countOfA[indexItem + 1]
            if s[indexItem] == 'a':
                countOfA[indexItem] += 1
                
        result = stringLength
        for indexItem in range(stringLength - 1):
            totalDeletions = countOfB[indexItem] + countOfA[indexItem + 1]
            result = min(totalDeletions, result)
            
        result = min(result, countOfB[-1], countOfA[0])
        return result
