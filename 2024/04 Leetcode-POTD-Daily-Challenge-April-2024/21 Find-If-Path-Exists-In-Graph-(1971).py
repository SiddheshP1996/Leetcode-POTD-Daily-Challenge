class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parents = [-1] * n

        def find(i):
            comp = []
            while parents[i] >= 0:
                comp.append(i)
                i = parents[i]
            while len(comp) > 0:
                parents[comp.pop()] = i
            return i
        def union(i, j):
            if i == j:
                return
            if parents[j] < parents[i]:
                return union(j, i)
            parents[i] += parents[j]
            parents[j] = i

        for u, v in edges:
            union(find(u), find(v))

        return find(source) == find(destination)
