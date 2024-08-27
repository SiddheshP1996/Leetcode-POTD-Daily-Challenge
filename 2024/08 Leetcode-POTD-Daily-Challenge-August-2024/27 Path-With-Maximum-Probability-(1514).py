class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        distance = [0] * n
        distance[start_node] = 1
        
        for _ in range(n - 1):
            updated = False
            for i, (sourceNode, targetNode) in enumerate(edges):
                if distance[sourceNode] * succProb[i] > distance[targetNode]:
                    distance[targetNode] = distance[sourceNode] * succProb[i]
                    updated = True
                    
                if distance[targetNode] * succProb[i] > distance[sourceNode]:
                    distance[sourceNode] = distance[targetNode] * succProb[i]
                    updated = True
                    
            if not updated:
                break
        
        return distance[end_node]
