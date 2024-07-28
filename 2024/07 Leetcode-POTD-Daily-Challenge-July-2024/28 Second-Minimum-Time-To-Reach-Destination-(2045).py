from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adjacentList = defaultdict(list)
        for u, v in edges:
            adjacentList[u - 1].append(v - 1)
            adjacentList[v - 1].append(u - 1)

        distanceOne = [(10 ** 20)] * n
        distanceTwo = [(10 ** 20)] * n
        minimumHeap = [(0, 0, 0, change)]
        distanceOne[0] = 0

        def dijkstraAlgo():
            while minimumHeap:
                currentDistance, currentNode, element, remainingGreen = heappop(minimumHeap)
                
                if element == 0 and currentDistance > distanceOne[currentNode]:
                    continue
                
                if element == 1 and currentDistance > distanceTwo[currentNode]:
                    continue
                
                if element == 1 and currentNode == n - 1:
                    return currentDistance
               
                if currentDistance // change % 2 == 1:
                    waitTime = change - currentDistance % change
                    currentDistance += waitTime
                    remainingGreen = change
                
                remainingGreen -= time
                
                for neighbor in adjacentList[currentNode]:
                    distance = currentDistance + time
                    if distance < distanceOne[neighbor]:
                        distanceTwo[neighbor] = distanceOne[neighbor]
                        distanceOne[neighbor] = distance
                        heappush(minimumHeap, (distance, neighbor, 0, remainingGreen))
                    elif distance > distanceOne[neighbor] and  distance < distanceTwo[neighbor]:
                        distanceTwo[neighbor] = distance
                        heappush(minimumHeap, (distance, neighbor, 1, remainingGreen))

            return -1

        return dijkstraAlgo()
