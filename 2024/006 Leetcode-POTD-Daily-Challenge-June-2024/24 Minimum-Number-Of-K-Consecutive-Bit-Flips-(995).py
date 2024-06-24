from collections import deque

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        queue = deque()
        target = 0
        result = 0
        for i in range(n):
            if len(queue) > 0 and queue[0] == i:
                queue.popleft()
                target = (target + 1) % 2

            if nums[i] == target:
                target = (target + 1) % 2
                queue.append(i + k)
                result += 1
        if len(queue) > 0 and queue[0] == n:
            queue.popleft()
        if len(queue) == 0:
            return result
        return -1
