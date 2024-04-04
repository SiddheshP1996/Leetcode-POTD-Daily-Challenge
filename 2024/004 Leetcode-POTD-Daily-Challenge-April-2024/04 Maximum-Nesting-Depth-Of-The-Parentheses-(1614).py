class Solution:
    def maxDepth(self, s: str) -> int:
        openParentheses = []
        result = 0
        for character in s:
            if character == '(':
                openParentheses.append(character)
            elif character == ')':
                if len(openParentheses) > 0:
                    result = max(result, len(openParentheses))
                    openParentheses.pop()
        return result
