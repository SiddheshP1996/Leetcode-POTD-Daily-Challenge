from heapq import heappop, heappush, heapify

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heapQueue = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapify(heapQueue)
        
        result = -1e9, 1e9
        right = max(row[0] for row in nums)
        
        while heapQueue:
            left, i, j = heappop(heapQueue)
            if (right - left) < (result[1] - result[0]):
                result = left, right
            if j + 1 == len(nums[i]):
                return result
            nextNum = nums[i][j + 1]
            right = max(right, nextNum)
            heappush(heapQueue, (nextNum, i, j + 1))
