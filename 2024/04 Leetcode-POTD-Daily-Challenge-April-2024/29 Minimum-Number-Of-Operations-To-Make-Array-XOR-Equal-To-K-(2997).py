class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        targetIndex = [0] * 32
        currentIndex = [0] * 32
        for i in range(32):
            targetIndex[i] = min((1 << i) & k, 1)
        currentXOR = nums[0]
        n = len(nums)
        for i in range(1, n):
            currentXOR ^= nums[i]
        for i in range(32):
            currentIndex[i] = min((1 << i) & currentXOR, 1)
        result = 0
        for i in range(32):
            if currentIndex[i] != targetIndex[i]:
                result += 1
        return result
