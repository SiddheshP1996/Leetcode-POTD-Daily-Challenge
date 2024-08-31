class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictNums = {}
        
        for index, num in enumerate(nums):
            dictNums[num] = index
            
        for index, num in enumerate(nums):
            if target - num in dictNums and index != dictNums[target - num]:
                return[index, dictNums[target - num]]
        