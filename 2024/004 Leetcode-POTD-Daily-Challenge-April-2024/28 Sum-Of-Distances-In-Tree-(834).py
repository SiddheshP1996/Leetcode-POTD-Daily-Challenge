from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adjacentList = defaultdict(list)
        N = n
        for u, v in edges:
            adjacentList[u].append(v)
            adjacentList[v].append(u)

        nodesCounter = [1] * N
        subtreeCounter = [0] * N
        result = [0] * N

        def get_sum(node, parentNode):
            result = 0
            for childNode in adjacentList[node]:
                if childNode == parentNode:
                    continue
                get_sum(childNode, node)
                nodesCounter[node] += nodesCounter[childNode]
                subtreeCounter[node] += subtreeCounter[childNode] + nodesCounter[childNode]
            return result

        def fix_sum(node, parentNode):
            if parentNode != -1:
                baseNode = subtreeCounter[parentNode]
                closeNodes = nodesCounter[node]
                furtherNodes = N - closeNodes
                subtreeCounter[node] = baseNode - closeNodes + furtherNodes
            for childNode in adjacentList[node]:
                if childNode == parentNode:
                    continue
                fix_sum(childNode, node)

        get_sum(0, -1)
        result[0] = subtreeCounter[0]
        fix_sum(0, -1)
        return subtreeCounter
