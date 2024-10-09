class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unmatchedOpenBrackets = unmatchedCloseBrackets = 0
        for character in s:
            if character == '(':
                unmatchedOpenBrackets += 1
            elif unmatchedOpenBrackets > 0:
                unmatchedOpenBrackets -= 1    
            else:
                unmatchedCloseBrackets += 1
        return unmatchedOpenBrackets + unmatchedCloseBrackets
