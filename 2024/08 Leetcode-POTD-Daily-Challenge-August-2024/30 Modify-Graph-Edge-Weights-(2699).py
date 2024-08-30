from heapq import heappop, heappush

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        adjacencyList = [[] for _ in range(n)]
        for i, (nodeA, nodeB, weight) in enumerate(edges):
            adjacencyList[nodeA].append((nodeB, i))
            adjacencyList[nodeB].append((nodeA, i))

        distances = [[float('inf')] * 2 for _ in range(n)]
        distances[source][0] = distances[source][1] = 0

        self.runDijkstra(adjacencyList, edges, distances, source, 0, 0)
        difference = target - distances[destination][0]

        if difference < 0:
            return []

        self.runDijkstra(adjacencyList, edges, distances, source, difference, 1)

        if distances[destination][1] < target:
            return []

        for edge in edges:
            if edge[2] == -1:
                edge[2] = 1

        return edges

    def runDijkstra(self, adjacencyList, edges, distances, source, difference, run):
        n = len(adjacencyList)
        priorityQueue = [(0, source)]
        distances[source][run] = 0

        while priorityQueue:
            currentDistance, currentNode = heappop(priorityQueue)
            if currentDistance > distances[currentNode][run]:
                continue

            for nextNode, edgeIndex in adjacencyList[currentNode]:
                weight = edges[edgeIndex][2]
                if weight == -1:
                    weight = 1
                    
                if run == 1 and edges[edgeIndex][2] == -1:
                    newWeight = difference + distances[nextNode][0] - distances[currentNode][1]
                    if newWeight > weight:
                        edges[edgeIndex][2] = weight = newWeight

                if distances[nextNode][run] > distances[currentNode][run] + weight:
                    distances[nextNode][run] = distances[currentNode][run] + weight
                    heappush(priorityQueue, (distances[nextNode][run], nextNode))
