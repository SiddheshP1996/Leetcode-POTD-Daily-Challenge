import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        minleap = []
        heapq.heappush(minleap, [0, points[0]])

        for i in range(1, len(points)):
            heapq.heappush(minleap, [distance(points[0], points[i]), points[i]])

        res = 0
        while minleap:
            cur = heapq.heappop(minleap)
            res += cur[0]
            for n in minleap:
                d = distance(cur[1], n[1])
                if n[0] > d:
                    n[0] = d
            heapq.heapify(minleap)
        return res
