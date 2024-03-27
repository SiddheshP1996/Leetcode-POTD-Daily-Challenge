class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        num_item = 0
        result = 0
        product = 1
        
        for num in range(len(nums)):
            product *= nums[num]
            
            if product >= k:
                while product >= k and num_item <= num:
                    product /= nums[num_item]
                    num_item += 1
            
            result += num - num_item + 1
        
        return result
