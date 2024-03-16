class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sumIndicesMap = {}
        sumVal = 0
        maxLength = 0
        for i, num in enumerate(nums):
            sumVal += 1 if num == 1 else -1
            if sumVal == 0:
                maxLength = i + 1
            elif sumVal in sumIndicesMap:
                maxLength = max(maxLength, i - sumIndicesMap[sumVal])
            else:
                sumIndicesMap[sumVal] = i
        return maxLength
