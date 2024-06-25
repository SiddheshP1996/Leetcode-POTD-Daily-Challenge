class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        expression = []

        for token_expression in tokens:
            if token_expression in {'/', '*', '+', '-'}:
                a = expression.pop()
                b = expression.pop()
                if token_expression == '/':
                    result = b / a
                    expression.append(math.floor(result) if result >= 0 else math.ceil(result))
                elif token_expression == '*':
                    expression.append(a * b)
                elif token_expression == '+':
                    expression.append(a + b)
                elif token_expression == '-':
                    expression.append(b - a)
            else:
                expression.append(int(token_expression))
        return expression.pop()
