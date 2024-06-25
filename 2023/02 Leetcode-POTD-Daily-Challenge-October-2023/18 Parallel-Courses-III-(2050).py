import heapq


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        N = n
        timeline = []
        START = 1
        END = -1
        unlocks = [[] for _ in range(N + 1) ]
        dependencies = [0] * (N + 1)
        for prev, cur in relations:
            dependencies[cur] += 1
            unlocks[prev].append(cur)
        currentTime = 0
        for i in range(1, N + 1):
            if dependencies[i] == 0:
                heapq.heappush(timeline, (currentTime, START, i))
                heapq.heappush(timeline, (currentTime + time[i - 1], END, i))
        while len(timeline) > 0:
            eventTime, event, course = heapq.heappop(timeline)
            currentTime = max(currentTime, eventTime)
            if event == END:
                for unlocked in unlocks[course]:
                    dependencies[unlocked] -= 1
                    if dependencies[unlocked] == 0:
                        heapq.heappush(timeline, (eventTime, START, unlocked))
                        heapq.heappush(timeline, (eventTime + time[unlocked - 1], END, unlocked))
        return currentTime
