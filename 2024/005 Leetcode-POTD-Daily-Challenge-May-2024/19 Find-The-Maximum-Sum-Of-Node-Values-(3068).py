class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        totalSum = 0
        count = 0
        minimumPositive = float("inf")
        maximumNegative = float("-inf")

        for nodeValue in nums:
            nodeValueOperation = nodeValue ^ k

            totalSum += nodeValue
            netChange = nodeValueOperation - nodeValue

            if netChange > 0:
                minimumPositive = min(minimumPositive, netChange)
                totalSum += netChange
                count += 1
            else:
                maximumNegative = max(maximumNegative, netChange)

        if count % 2 == 0:
            return totalSum
        return max(totalSum - minimumPositive, totalSum + maximumNegative)
