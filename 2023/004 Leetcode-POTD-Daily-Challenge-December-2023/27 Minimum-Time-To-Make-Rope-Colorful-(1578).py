class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        numberOfRope = [0]
        result = 0
        for i in range(1, n):
            if colors[i] == colors[numberOfRope[-1]]:
                if neededTime[i] <= neededTime[numberOfRope[-1]]:
                    result += neededTime[i]
                    continue
                else:
                    result += neededTime[numberOfRope.pop()]
            numberOfRope.append(i)
        return result
