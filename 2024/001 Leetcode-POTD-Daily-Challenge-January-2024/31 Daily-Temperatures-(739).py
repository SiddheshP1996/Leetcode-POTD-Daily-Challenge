class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result stands for result where array is stored and len stands length of array
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                result[stack.pop()] = i - stack[-1]
            stack.append(i)
        return result
