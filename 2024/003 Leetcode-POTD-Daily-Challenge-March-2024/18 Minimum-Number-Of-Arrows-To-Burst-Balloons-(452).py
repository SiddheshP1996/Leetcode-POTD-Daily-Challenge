from heapq import heappop

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        timeline = []
        START = -1
        END = 1
        n = len(points)
        for i in range(n):
            startPoint, endPoint = points[i]
            timeline.append((startPoint, START, i))
            timeline.append((endPoint, END, i))
        heapq.heapify(timeline)
        state = 0
        result = 0
        shot = [False] * n
        all_id = []
        while len(timeline) > 0:
            heapTime, event, id = heapq.heappop(timeline)
            if event == START:
                all_id.append(id)
            elif not shot[id]:
                needed = 1
                while len(all_id) > 0:
                    id = all_id.pop()
                    shot[id] = True
                result += needed

        return result
