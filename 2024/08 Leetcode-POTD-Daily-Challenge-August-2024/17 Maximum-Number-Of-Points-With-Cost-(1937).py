class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = len(points[0])

        for i in range(1, n):
            leftDP = [0] * m
            leftDP[0] = points[i - 1][0]
            for j in range(1, m):
                leftDP[j] = max(leftDP[j - 1] - 1, points[i - 1][j])

            rightDP = [0] * m
            rightDP[m - 1] = points[i - 1][m - 1]
            for j in range(m - 2, -1, -1):
                rightDP[j] = max(rightDP[j + 1] - 1, points[i - 1][j])

            for j in range(m):
                points[i][j] += max(leftDP[j], rightDP[j])

        return max(points[-1])
