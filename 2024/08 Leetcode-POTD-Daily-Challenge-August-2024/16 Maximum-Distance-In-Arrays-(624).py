class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        INF = (10 ** 20)
        result = -INF
        arrays.sort(key=lambda x: (x[0], x[-1]))
        maxSeen = arrays[0][-1]
        for i in range(1, n):
            result = max(result, abs(maxSeen - arrays[i][0]))
            result = max(result, abs(arrays[0][0] - arrays[i][-1]))
            maxSeen = max(maxSeen, arrays[i][-1])

        return result
