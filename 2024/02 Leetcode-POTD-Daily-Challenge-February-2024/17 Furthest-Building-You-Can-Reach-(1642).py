from heapq import heappop, heappush

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if len(heights) == 1:
            return 0
        
        priorityQueue = []
        distance = 0
        
        while distance < len(heights) - 1:
            if heights[distance + 1] <= heights[distance]:
                distance += 1
                continue
            heightDifference = heights[distance + 1] - heights[distance]
        
            if bricks >= heightDifference:
                bricks -= heightDifference
                heapq.heappush(priorityQueue, -heightDifference)
        
            elif ladders > 0:
                if priorityQueue:
                    pastBricks = -priorityQueue[0]
                    if pastBricks > heightDifference:
                        bricks += pastBricks
                        heapq.heappop(priorityQueue)
                        bricks -= heightDifference
                        heapq.heappush(priorityQueue, -heightDifference)
                ladders -= 1
        
            else:
                break
            distance += 1

        return distance
