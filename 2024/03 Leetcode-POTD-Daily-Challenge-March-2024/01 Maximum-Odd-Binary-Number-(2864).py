class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeros = s.count("0")
        ones = s.count("1")
        result = []
        for one in range(ones - 1):
            result.append("1")
        for zero in range(zeros):
            result.append("0")
        result.append("1")
        return "".join(result)
