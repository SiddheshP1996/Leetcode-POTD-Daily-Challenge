class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        maxAtLeft = n
        minAtRight = 0
        if len(left) > 0:
            maxAtLeft = max(left)
        else:
            return n - min(right) if len(right) > 0 else 0
        if len(right) > 0:
            minAtRight = min(right)
        else:
            return maxAtLeft

        return max(n - minAtRight, maxAtLeft)
    