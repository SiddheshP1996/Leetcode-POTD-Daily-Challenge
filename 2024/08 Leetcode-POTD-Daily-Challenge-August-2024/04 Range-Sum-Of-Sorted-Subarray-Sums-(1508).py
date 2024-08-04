class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = ((10 ** 9) + 7)
        totalNumber = len(nums)
        allSubArrays = []
        
        for i in range(totalNumber):
            start = 0
            for j in range(i, totalNumber):
                start += nums[j]
                allSubArrays.append(start)
        subArrayLength = len(allSubArrays)
        allSubArrays.sort()
        
        preSum = [0] * subArrayLength
        preSum[0] = allSubArrays[0]
        for i in range(1, subArrayLength):
            preSum[i] = preSum[i - 1] + allSubArrays[i]
            
        left -= 1
        right -= 1
        
        return (preSum[right] - (preSum[left - 1] if left > 0 else 0)) % (mod)
