class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        def go(i, j, k):
            if k == n:
                return 0
            if [i, j] == points[k]:
                return go(i, j, k + 1)
            targetPoints = points[k]
            verticalMovement = targetPoints[0] - i
            horizontalMovement = targetPoints[1] - j
            if verticalMovement < 0:
                verticalMovement = -1
            if verticalMovement > 0:
                verticalMovement = 1
            if horizontalMovement < 0:
                horizontalMovement = -1
            if horizontalMovement > 0:
                horizontalMovement = 1
            return 1 + go(i + verticalMovement, j + horizontalMovement, k)

        return go(points[0][0], points[0][1], 1)
