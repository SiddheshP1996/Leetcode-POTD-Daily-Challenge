class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        N = n
        for i in range(len(edges)):
            t,u,v = edges[i]
            edges[i] = [t, u - 1, v - 1]
        bobParents = [-1] * N
        aliceParents = [-1] * N

        def find(i,parents):
            path_comp = []
            while parents[i] >= 0:
                i = parents[i]
            while(len(path_comp) > 0):
                parents[path_comp.pop()] = i
            return i

        def union(u, v, parents):
            if u == v:
                return 1
            if parents[v] < parents[u]:
                return union(v, u, parents)
            parents[u] += parents[v]
            parents[v] = u
            return 0
        canDeleteBoth = 0
        for t, u, v in edges:
            if t == 3:
                canDeleteBoth += union(find(u, aliceParents), find(v, aliceParents),aliceParents)
                union(find(u, bobParents), find(v, bobParents),bobParents)
        canDeleteAlice = 0
        canDeleteBob = 0
        for t, u, v in edges:
            if t == 1:
                canDeleteAlice += union(find(u, aliceParents), find(v, aliceParents), aliceParents)
            if t == 2:
                canDeleteBob += union(find(u, bobParents), find(v, bobParents), bobParents)

        bobRoot = 0
        aliceRoot = 0
        for i in range(N):
            if aliceParents[i] < 0:
                aliceRoot += 1
            if bobParents[i] < 0:
                bobRoot += 1

        if bobRoot != 1 or aliceRoot != 1:
            return -1
        return canDeleteBoth + canDeleteAlice + canDeleteBob
