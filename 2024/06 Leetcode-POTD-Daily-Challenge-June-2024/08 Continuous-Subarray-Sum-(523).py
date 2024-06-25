class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mapIndex = {0:-1}
        n = len(nums)
        current = 0
        for i in range(n):
            x = nums[i]
            current += x
            current %= k
            if current in mapIndex:
                if (i - mapIndex[current] ) >= 2:
                    return True
            else:
                mapIndex[current] = i
        return False
