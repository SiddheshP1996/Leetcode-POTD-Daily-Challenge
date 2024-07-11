class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ')':
                temporaryElement = ""
                while stack[-1] != '(':
                    temporaryElement += stack.pop()
                stack.pop()
                for j in temporaryElement: stack.append(j)
            else: stack.append(i)
        return "".join(stack)
