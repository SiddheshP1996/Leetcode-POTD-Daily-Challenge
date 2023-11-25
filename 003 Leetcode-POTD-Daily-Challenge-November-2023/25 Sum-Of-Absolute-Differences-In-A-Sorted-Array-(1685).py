class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        absoluteDifference = 0
        n = len(nums)
        previousSum = [0] * n
        previousSum[0] = nums[0]
        for i in range(1, n):
            previousSum[i] = previousSum[i - 1] + nums[i]

        results = [-1] * n
        ahead = 0
        for i in range(n - 1, -1, -1):
            if i + 1 < n:
                elementsAhead = (n - 1 - i)
                diff = abs(nums[i] - ahead)
                absoluteDifference += (diff * (elementsAhead - 1)) + diff
            finalResults = abs(((i + 1) * nums[i]) - (previousSum[i])) + absoluteDifference
            results[i] = finalResults
            ahead = nums[i]

        return results
    