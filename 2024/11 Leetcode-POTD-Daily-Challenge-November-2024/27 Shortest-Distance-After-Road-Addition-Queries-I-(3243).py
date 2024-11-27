class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for i in range(n - 1): 
            graph[i].append(i + 1)
        
        def bfs(graph):
            queue = deque([0])
            seen = {0}
            result = 0 
            while queue: 
                for _ in range(len(queue)): 
                    currentNode = queue.popleft()
                    if currentNode == n - 1: return result 
                    for adjacentNode in graph[currentNode]: 
                        if adjacentNode not in seen: 
                            seen.add(adjacentNode)
                            queue.append(adjacentNode)
                result += 1
                
        result = []   
        for currentNode, adjacentNode in queries: 
            graph[currentNode].append(adjacentNode)
            result.append(bfs(graph))
        return result
