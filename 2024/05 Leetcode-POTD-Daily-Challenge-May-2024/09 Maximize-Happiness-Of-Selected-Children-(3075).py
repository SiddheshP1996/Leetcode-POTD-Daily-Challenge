from heapq import heapify, heappop

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happyHeap = [-h for h in happiness]
        heapify(happyHeap)
        result = 0
        for i in range(min(k, len(happiness))):
            result += max(0, abs(heappop(happyHeap)) - i)
        return result
