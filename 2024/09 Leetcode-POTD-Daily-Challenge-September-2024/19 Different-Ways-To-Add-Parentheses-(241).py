class Solution:
    def __init__(self):
        self.map = {}

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression in self.map:
            return self.map[expression]

        result = []

        for i in range(len(expression)):
            character = expression[i]

            if character in "*+-":
                leftOfExpr = self.diffWaysToCompute(expression[:i])
                rightOfExpr = self.diffWaysToCompute(expression[i + 1:])

                for leftSubExpr in leftOfExpr:
                    for rightSubExpr in rightOfExpr:
                        if character == "+":
                            result.append(leftSubExpr + rightSubExpr)
                        elif character == "-":
                            result.append(leftSubExpr - rightSubExpr)
                        elif character == "*":
                            result.append(leftSubExpr * rightSubExpr)

        if not result:
            result.append(int(expression))

        self.map[expression] = result

        return result
