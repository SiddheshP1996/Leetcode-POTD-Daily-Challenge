class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current, count = nums[0], 1
        for i in nums[1:]:
            count += (1 if current == i else -1)
            if not count:
                current = i
                count = 1
        return current
