class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mask = 0
        for n in nums:
            if mask & (1 << n) != 0:
                return n
            mask |= (1 << n)
        return -1
