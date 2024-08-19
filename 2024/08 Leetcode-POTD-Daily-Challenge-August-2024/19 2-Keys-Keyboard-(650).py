class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        self.targetLength = n
        
        def findMinSteps(currentLength: int, clipboardLength: int) -> int:
            if currentLength == self.targetLength:
                return 0
            if currentLength > self.targetLength:
                return float('inf')
            
            copyAndPaste = 2 + findMinSteps(currentLength * 2, currentLength)
            pasteOnly = 1 + findMinSteps(currentLength + clipboardLength, clipboardLength)
            
            return min(copyAndPaste, pasteOnly)
        
        return 1 + findMinSteps(1, 1)
