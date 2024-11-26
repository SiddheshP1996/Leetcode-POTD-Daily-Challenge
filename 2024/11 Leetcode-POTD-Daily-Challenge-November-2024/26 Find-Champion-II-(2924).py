class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inDegree = [0] * n
        
        for startEdge, endEdge in edges:
            inDegree[endEdge] += 1
        
        champions = [i for i in range(n) if inDegree[i] == 0]
        
        if len(champions) == 1:
            return champions[0]
        else:
            return -1
