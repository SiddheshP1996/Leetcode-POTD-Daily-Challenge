class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()

        result = 0
        previousPoint = points[0][0]

        for x, _ in points:
            result = max((x - previousPoint), result)
            previousPoint = x
        return result
