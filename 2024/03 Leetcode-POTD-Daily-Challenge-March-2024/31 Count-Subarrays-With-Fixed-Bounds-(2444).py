class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minIndex, maxIndex, leftSideNum, rightSideNum = -1, -1, -1, 0
        count = 0
        
        while rightSideNum < len(nums):
            if nums[rightSideNum] < minK or nums[rightSideNum] > maxK:
                minIndex = rightSideNum
                maxIndex = rightSideNum
                leftSideNum = rightSideNum
            
            minIndex = rightSideNum if nums[rightSideNum] == minK else minIndex
            maxIndex = rightSideNum if nums[rightSideNum] == maxK else maxIndex
            
            count += min(minIndex, maxIndex) - leftSideNum
            rightSideNum += 1
        
        return count
