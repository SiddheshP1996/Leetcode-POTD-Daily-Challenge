from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjacentList = defaultdict(list)
        for source, destination, weight in edges:
            adjacentList[source].append((destination, weight))
            adjacentList[destination].append((source, weight))

        def dijkstraAlgo(start):
            minimumHeap = [(0, start)]
            distances = [(10 ** 20)] * n
            distances[start] = 0

            while minimumHeap:
                currentDistance, currentNode = heappop(minimumHeap)

                if currentDistance > distances[currentNode]:
                    continue

                for neighbor, weight in adjacentList[currentNode]:
                    distance = currentDistance + weight

                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heappush(minimumHeap, (distance, neighbor))

            reachableCities = sum(dist <= distanceThreshold for dist in distances) - 1
            return reachableCities

        minimumReachable = 10 ** 20
        result = -1

        for i in range(n):
            reachableCount = dijkstraAlgo(i)
            if reachableCount <= minimumReachable:
                minimumReachable = reachableCount
                result = i

        return result
