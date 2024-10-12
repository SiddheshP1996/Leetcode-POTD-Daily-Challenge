from heapq import heappop, heappush

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        priorityQueue = []
        for start, end in intervals:
            if priorityQueue and priorityQueue[0] < start:
                heappop(priorityQueue)
            heappush(priorityQueue, end)
        return len(priorityQueue)
