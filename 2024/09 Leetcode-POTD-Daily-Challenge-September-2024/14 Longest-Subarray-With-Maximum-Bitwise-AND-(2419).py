class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximumValue = -float('inf')
        longest = currentLength = 0
        
        for num in nums:
            if num > maximumValue:
                maximumValue = num
                currentLength = 1
                longest = 1
            elif num == maximumValue:
                currentLength += 1
                longest = max(longest, currentLength)
            else:
                currentLength = 0
        
        return longest
    
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxValue = max(nums)
        maxLength = currentLength = 0
        
        for num in nums:
            if num == maxValue:
                currentLength += 1
                maxLength = max(maxLength, currentLength)
            else:
                currentLength = 0
        
        return maxLength
"""
