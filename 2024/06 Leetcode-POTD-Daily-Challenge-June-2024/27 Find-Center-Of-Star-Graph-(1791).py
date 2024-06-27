from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjacentList = defaultdict(list)
        
        for u,v in edges:
            adjacentList[u].append(v)
            adjacentList[v].append(u)
        
        for x in adjacentList.keys():
            if len(adjacentList[x]) == (len(adjacentList) - 1):
                return x
        return -1
