class Solution:
    def checkValidString(self, s: str) -> bool:
        leftParenthesesStack, asteriskStack = [], []
        
        for i in range(len(s)):
            if s[i] == '(':
                leftParenthesesStack.append(i)
            elif s[i] == '*':
                asteriskStack.append(i)
            else:
                if leftParenthesesStack:
                    leftParenthesesStack.pop()
                elif asteriskStack:
                    asteriskStack.pop()
                else:
                    return False
        
        while leftParenthesesStack and asteriskStack:
            if leftParenthesesStack[-1] > asteriskStack[-1]:
                return False
            leftParenthesesStack.pop()
            asteriskStack.pop()
            
        return not leftParenthesesStack
