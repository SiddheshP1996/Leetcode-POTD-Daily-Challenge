class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dictonary = { 0: 1 }
        count = result = 0
        for index, num in enumerate(nums):
            if num % 2 == 1:
                count += 1
                
            if count - k in dictonary:
                result += dictonary[count - k]
            
            dictonary[count] = dictonary.get(count, 0) + 1
            
        return result
