from collections import deque

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        result = 0
        histogram = [0] * len(matrix[0])
        
        for row in matrix:
            for i in range(len(row)):
                histogram[i] = histogram[i] + 1 if row[i] == '1' else 0
            result = max(result, self.largestRectangleArea(histogram))
        
        return result
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = deque()
        
        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                result = max(result, height * width)
            stack.append(i)
        
        return result
