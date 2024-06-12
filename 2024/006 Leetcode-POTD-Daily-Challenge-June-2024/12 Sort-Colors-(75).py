from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = collections.Counter(nums)
        index = 0
        for k in range(3):
            c = count[k]
            for i in range(c):
                nums[index] = k
                index += 1
