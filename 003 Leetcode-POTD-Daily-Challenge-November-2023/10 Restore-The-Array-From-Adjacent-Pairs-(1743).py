import collections


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # N = len(adjacentPairs)
        seen = collections.defaultdict(int)
        adjacentList = collections.defaultdict(set)
        nodes = set()
        for u, v in adjacentPairs:
            seen[v] += 1
            seen[u] += 1
            adjacentList[u].add(v)
            adjacentList[v].add(u)
            nodes.add(u)
            nodes.add(v)
        startNode = None
        for node in nodes:
            if seen[node] == 1:
                startNode = node
                break
        results = []

        def dfs(node):
            if node is None:
                return
            results.append(node)
            nodes.discard(node)
            for nnode in adjacentList[node]:
                if nnode in nodes:
                    dfs(nnode)

        dfs(startNode)
        return results
