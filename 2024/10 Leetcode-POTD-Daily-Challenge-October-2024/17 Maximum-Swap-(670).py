class Solution:
    def maximumSwap(self, num: int) -> int:
        numList = list(str(num))
        last = {int(d): i for i, d in enumerate(numList)}
        
        for i, digit in enumerate(numList):
            for d in range(9, int(digit), -1):
                if last.get(d, -1) > i:
                    numList[i], numList[last[d]] = numList[last[d]], numList[i]
                    return int(''.join(numList))
        
        return num
