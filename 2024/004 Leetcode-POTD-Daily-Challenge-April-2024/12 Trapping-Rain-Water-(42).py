class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxBefore = [0] * n
        maxAfter = [0] * n
        maxBefore[0] = height[0]
        maxAfter[-1] = height[-1]
        for i in range(1, n):
            maxBefore[i] = max(maxBefore[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            maxAfter[i] = max(maxAfter[i + 1], height[i])
        result = [0] * n

        for i in range(1, n - 1):
            trapped = min(maxBefore[i - 1], maxAfter[i + 1]) - height[i]
            result[i] = max(trapped, 0)
        return sum(result)
