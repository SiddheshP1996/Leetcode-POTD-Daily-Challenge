class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        numberOfOnes = nums.count(1)
        totalNumbers = len(nums)
        right = 0
        windowOnes = 0
        bestNumber = totalNumbers
        while right < (totalNumbers * 2):
            if nums[right % totalNumbers] == 1:
                windowOnes += 1
                
            if (right + 1) < numberOfOnes:
                right += 1
                continue
            
            if (right + 1) > numberOfOnes:
                if nums[(right - numberOfOnes) % totalNumbers] == 1:
                    windowOnes -= 1
                    
            bestNumber = min(bestNumber, numberOfOnes - windowOnes)
            right += 1
        return bestNumber
