import math


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        incrementNumber = int(math.ceil(n // 4))
        i = 0
        while i < n:
            numberAhead = min(i + incrementNumber, n - 1)
            if arr[i] == arr[numberAhead]:
                return arr[i]
            leftSideNumber = i
            rightSideNumber = numberAhead
            while leftSideNumber < rightSideNumber:
                middleNumber = (leftSideNumber + rightSideNumber) // 2
                if arr[middleNumber] > arr[i]:
                    rightSideNumber = middleNumber
                else:
                    leftSideNumber = middleNumber + 1
            i = leftSideNumber

        return arr[0]
