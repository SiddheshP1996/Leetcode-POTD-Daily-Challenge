class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        expressions = []
        expressionStack = []
        for i in expression:
            if i in ['&', '|', '!']:
                expressions.append(i)
            elif i == ')':
                x = expressionStack.pop()
                if expressions[-1] == '&':
                    temp = True
                elif expressions[-1] == '|':
                    temp = False
                else:
                    expressionStack.pop()
                    expressions.pop()
                    var = 'f' if x == 't' else 't'
                    expressionStack.append(var)
                    continue
                while x != '(':
                    var = False if x == 'f' else True
                    if expressions[-1] == '&':
                        temp = temp and var
                    else:
                        temp = temp or var
                    x = expressionStack.pop()
                var = 't' if temp == True else 'f'
                expressionStack.append(var)
                expressions.pop()
            elif i != ',':
                expressionStack.append(i)
        return True if expressionStack[-1] == 't' else False
