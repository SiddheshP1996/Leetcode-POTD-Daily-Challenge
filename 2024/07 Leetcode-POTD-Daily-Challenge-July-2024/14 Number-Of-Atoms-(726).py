class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [{}]
        i, n = 0, len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append({})
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                iStart = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[iStart:i] or 1)
                for element, count in top.items():
                    stack[-1][element] = stack[-1].get(element, 0) + count * multiplier
            else:
                iStart = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                element = formula[iStart:i]
                iStart = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[iStart:i] or 1)
                stack[-1][element] = stack[-1].get(element, 0) + count

        result = stack.pop()
        sortedElements = sorted(result.keys())
        return ''.join(f"{element}{(result[element] if result[element] > 1 else '')}" for element in sortedElements)
