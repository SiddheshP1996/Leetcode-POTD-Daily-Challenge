from collections import Counter
from heapq import heappop, heappush

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        count = Counter(nums)
        emptySlots = []
        maximumNumber = nums[-1]
        maximumSeen = nums[-1]
        
        for i in range(maximumNumber, -1, -1):
            num = i
            if count[num] > 1:
                while count[num] > 1:
                    nextSlot = 0
                    if len(emptySlots) > 0:
                        nextSlot = heappop(emptySlots)
                    else:
                        maximumSeen += 1
                        nextSlot = maximumSeen
                    result += nextSlot - num
                    count[num] -= 1
                    count[nextSlot] += 1
            elif count[num] == 0:
                heappush(emptySlots, num)
                
        return result
