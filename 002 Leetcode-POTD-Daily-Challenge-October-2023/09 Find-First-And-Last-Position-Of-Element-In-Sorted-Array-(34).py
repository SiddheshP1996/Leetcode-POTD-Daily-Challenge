class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        for i, n in enumerate(nums):
            if n == target:
                if result[0] == -1:
                    result[0] = i
                result[-1] = i
        return result
