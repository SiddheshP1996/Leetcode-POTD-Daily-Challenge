class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        openStrStack = []
        mustRemoveParantheses = set()
        for string in range(n):
            character = s[string]
            if character == '(':
                openStrStack.append(string)
            elif character == ')':
                if len(openStrStack) == 0:
                    mustRemoveParantheses.add(string)
                else:
                    openStrStack.pop()
        for remaining in openStrStack:
            mustRemoveParantheses.add(remaining)
        result = []
        for string in range(n):
            if string in mustRemoveParantheses:
                continue
            result.append(s[string])
        return "".join(result)
