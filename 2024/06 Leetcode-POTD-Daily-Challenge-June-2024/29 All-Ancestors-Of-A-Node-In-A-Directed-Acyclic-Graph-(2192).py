from sortedcontainers import SortedList, SortedSet
class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """

        adj_list = collections.defaultdict(list)
        result = [SortedSet() for _ in range(n)]
        inbound = [0] * n
        for u,v in edges:
            adj_list[u].append(v)
            inbound[v] += 1

        orderStart = SortedList([(inbound[i], i) for i in range(n)] )

        while len(orderStart) > 0:
            _, node = orderStart[0]
            orderStart.remove((_, node))
            for v in adj_list[node]:
                for x in result[node]:
                    result[v].add(x)
                orderStart.remove( (inbound[v], v) )
                inbound[v] -= 1
                result[v].add(node)
                orderStart.add((inbound[v], v))

        return result
