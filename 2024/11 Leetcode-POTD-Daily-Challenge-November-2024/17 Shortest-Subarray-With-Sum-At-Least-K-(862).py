class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        result = inf 
        queue = deque([(-1, 0)])
        prefix = 0
        for i, x in enumerate(nums): 
            prefix += x
            while queue and prefix - queue[0][1] >= k:
                result = min(result, i - queue.popleft()[0])
            while queue and queue[-1][1] >= prefix: queue.pop()
            queue.append((i, prefix))
        return result if result < inf else -1
