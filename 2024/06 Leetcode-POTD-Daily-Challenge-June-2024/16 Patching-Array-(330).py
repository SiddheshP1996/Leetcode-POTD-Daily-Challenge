class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        reachableMaximum = 0
        patches = 0
        i = 0

        while reachableMaximum < n:
            if i < len(nums) and nums[i] <= reachableMaximum + 1:
                reachableMaximum += nums[i]
                i += 1
            else:
                reachableMaximum += reachableMaximum + 1
                patches += 1

        return patches
