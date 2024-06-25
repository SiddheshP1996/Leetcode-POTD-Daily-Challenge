class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        numbersSeen = set()
        for i in range(0, c + 1):
            square = i * i
            numbersSeen.add(square)
            if (c - square) in numbersSeen:
                return True
            if square > c:
                break
        return False
