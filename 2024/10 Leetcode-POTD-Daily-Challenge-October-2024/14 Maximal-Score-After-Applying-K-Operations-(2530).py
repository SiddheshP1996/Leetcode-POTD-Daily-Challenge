from heapq import heapify, heapreplace

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        priorityQueue = [-x for x in nums]
        heapify(priorityQueue)
        result = 0 
        for i in range(k): 
            result -= priorityQueue[0] 
            heapreplace(priorityQueue, priorityQueue[0] // 3)
        return result
