class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        result = 0
        for i in range(len(nums))[::-1]:
            if not stack or nums[i] > stack[-1][0]:
                stack.append([nums[i], i])
            else:
                j = stack[bisect.bisect(stack, [nums[i], i])][1]
                result = max(result, j - i)
        return result
