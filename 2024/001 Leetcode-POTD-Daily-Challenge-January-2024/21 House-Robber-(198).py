class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        house_cache = [-1] * n

        def money_which_recovered(i):
            if i >= n:
                return 0
            if house_cache[i] >= 0:
                return house_cache[i]
            
            house_cache[i] = max(nums[i] + money_which_recovered(i + 2),
                      money_which_recovered(i + 1))
            return house_cache[i]
    
        return money_which_recovered(0)
