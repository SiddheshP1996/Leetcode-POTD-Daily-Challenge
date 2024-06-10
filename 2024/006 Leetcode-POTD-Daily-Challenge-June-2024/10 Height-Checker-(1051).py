class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        copyH = sorted(list(heights))
        n = len(heights)
        result = 0
        for i in range(n):
            if copyH[i] != heights[i]:
                result += 1
        return result
