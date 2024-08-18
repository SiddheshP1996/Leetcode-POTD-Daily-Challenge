from heapq import heappop, heappush

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNum, nextUglyNum, uglyNumSeen = [1], 1, set()
        for num in range(n):
            while nextUglyNum in uglyNumSeen: nextUglyNum = heappop(uglyNum)
            uglyNumSeen.add(nextUglyNum)
            for i in [2, 3, 5]: heappush(uglyNum, i * nextUglyNum)
        return nextUglyNum
