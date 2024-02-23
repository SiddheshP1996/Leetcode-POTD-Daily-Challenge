from collections import deque, defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0
        q = collections.deque()
        seen = {}
        adjacentLocation = collections.defaultdict(list)
        for flight, timeSpan, flightPersonal in flights:
            adjacentLocation[flight].append((timeSpan, flightPersonal))

        q.append((src, 0, 0))
        result = 10 ** 20

        while len(q) > 0:
            size = len(q)
            for _ in range(size):
                flightDirection, flightRoute, totalCost = q.popleft()
                if flightDirection == dst:
                    result = min(result, totalCost)
                if flightRoute == k + 1:
                    break
                seen[flightDirection] = totalCost
                for nextFlight, flightPrice in adjacentLocation[flightDirection]:
                    if nextFlight not in seen or (totalCost + flightPrice) <= seen[nextFlight]:
                        q.append((nextFlight, flightRoute + 1, totalCost + flightPrice))
        return result if result < 10 ** 20 else -1
