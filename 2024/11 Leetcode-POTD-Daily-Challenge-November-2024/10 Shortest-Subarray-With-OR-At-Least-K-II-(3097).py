class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def addRight(windowOR, num):
            windowOR = num | windowOR
            i = 0
            while num:
                bitCount[i] += num % 2
                num >>= 1
                i += 1
            return windowOR

        def removeLeft(windowOR, num):
            i = 0
            while num:
                bitCount[i] -= num % 2 
                if bitCount[i] == 0 and num % 2 == 1:
                    windowOR = windowOR ^ (1 << i)
                num >>= 1
                i += 1
            return windowOR

        bitCount = [0] * 32
        windowOR = 0
        shortest = float('inf')
        left, right = 0, 0

        while right < len(nums):
            windowOR = addRight(windowOR, nums[right])

            while left <= right and windowOR >= k:
                shortest = min(shortest, right - left + 1)
                windowOR = removeLeft(windowOR, nums[left])
                left += 1

            right += 1

        return shortest if shortest != float('inf') else -1
