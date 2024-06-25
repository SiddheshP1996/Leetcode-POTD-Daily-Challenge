class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # Initialize the adjacency Node list and degree of each node
        adjacencyNodeList = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            adjacencyNodeList[u].append(v)
            adjacencyNodeList[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # Initialize leaves queue
        initiateLeaves = deque([i for i in range(n) if degree[i] == 1])
        
        # Trim leaves until 2 or fewer nodes remain
        remainingNodes = n
        while remainingNodes > 2:
            numberOfLeaves = len(initiateLeaves)
            remainingNodes -= numberOfLeaves
            for _ in range(numberOfLeaves):
                leaf = initiateLeaves.popleft()
                for neighbor in adjacencyNodeList[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        initiateLeaves.append(neighbor)
        
        return list(initiateLeaves)
