# Solution No 1

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        results = 0

        for g in garbage:
            results += len(g)

        m, p, g = False, False, False

        for i in range(len(travel), 0, -1):
            m = m or 'M' in garbage[i]
            p = p or 'P' in garbage[i]
            g = g or 'G' in garbage[i]

            results += travel[i - 1] * (m + p + g)

        return results


# Solution No 2

"""
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)

        counter = collections.defaultdict(int)

        for i in range(n):
            countNoRow = collections.defaultdict(int)
            for c in garbage[i]:
                countNoRow[c] += 1
            counter[(i, 'P')] = countNoRow['P']
            counter[(i, 'M')] = countNoRow['M']
            counter[(i, 'G')] = countNoRow['G']

        travel.append(0)

        def go(i, t, b):
            if i == n:
                return 0
            key = (i, t)
            if counter[key] > 0:
                return counter[key] + b + go(i + 1, t, travel[i])
            return go(i + 1, t, b + travel[i])

        results = 0

        results += go(0, 'P', 0)
        results += go(0, 'M', 0)
        results += go(0, 'G', 0)
        return results
"""