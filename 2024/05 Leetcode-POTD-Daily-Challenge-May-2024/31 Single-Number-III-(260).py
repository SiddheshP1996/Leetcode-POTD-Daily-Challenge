class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = 0
        n = len(nums)
        for i in range(n):
            count ^= nums[i]
        position = 0
        for i in range(64):
            if ((1 << i) & count) != 0:
                position = i
                break
        base = 0
        for n in nums:
            if ((1 << position) & n) != 0:
                base ^= n
        return [count ^ base, base]
