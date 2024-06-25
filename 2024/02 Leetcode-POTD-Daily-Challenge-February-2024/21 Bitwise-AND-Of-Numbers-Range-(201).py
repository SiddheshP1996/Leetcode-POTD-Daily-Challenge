class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shiftNum = 0
        numL = left
        numR = right
        while (numL < numR):
            numL >>= 1
            numR >>= 1
            shiftNum += 1
        return numL << shiftNum
