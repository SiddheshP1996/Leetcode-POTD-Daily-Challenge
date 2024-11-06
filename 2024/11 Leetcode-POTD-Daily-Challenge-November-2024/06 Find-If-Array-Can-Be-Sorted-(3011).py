class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
                
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    if bin(nums[i]).count('1') != bin(nums[j]).count('1'):
                        return False
                    nums[i], nums[j] = nums[j], nums[i]
                    
        for k in range(len(nums) - 1):
            if nums[k] > nums[k + 1]:
                return False

        return True
