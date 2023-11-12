class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        maxStop = max(max(route) for route in routes)
        if maxStop < target:
            return -1

        n = len(routes)
        minBusesToReach = [float('inf')] * (maxStop + 1)
        minBusesToReach[source] = 0

        flag = True
        while flag:
            flag = False
            for route in routes:
                mini = float('inf')
                for stop in route:
                    mini = min(mini, minBusesToReach[stop])
                mini += 1
                for stop in route:
                    if minBusesToReach[stop] > mini:
                        minBusesToReach[stop] = mini
                        flag = True

        return minBusesToReach[target] if minBusesToReach[target] < float('inf') else -1
