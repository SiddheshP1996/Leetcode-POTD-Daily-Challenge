from heapq import heappush, heappop

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chair, temp, target = 0, 0, times[targetFriend]
        chairTaken, freeChair = [], []
        times = sorted(times, key=lambda x: x[0])
        
        for start, end in times:
            while chairTaken and chairTaken[0][0] <= start:
                heappush(freeChair, heappop(chairTaken)[1])    
            if freeChair:
                temp = heappop(freeChair)
                heappush(chairTaken, [end, temp])     
            else:
                temp = chair
                heappush(chairTaken, [end, chair])
                chair += 1
            if start == target[0]: return temp
