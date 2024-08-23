import re
from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        result = Fraction(0)
        
        tokens = re.findall(r'[+-]?\d+/\d+', expression)
        
        for token in tokens:
            result += Fraction(token)
        
        if result.denominator == 1:
            return f"{result.numerator}/1"
        else:
            return f"{result.numerator}/{result.denominator}"
