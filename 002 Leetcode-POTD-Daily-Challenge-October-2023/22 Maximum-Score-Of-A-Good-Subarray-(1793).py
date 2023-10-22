import heapq


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        INF = (10 ** 20)
        N = len(nums)
        numbers = []
        for i in range(N):
            numbers.append((nums[i], i))
        heapq.heapify(numbers)
        result = 0
        i = 0
        j = N - 1
        while len(numbers) > 0:
            if i > k or j < k:
                return result
            while numbers[0][1] < i or numbers[0][1] > j:
                heapq.heappop(numbers)
                if len(numbers) == 0:
                    return result
            result_here = (numbers[0][0] * ((j - i) + 1))
            result = max(result, result_here)
            _, shrink = heapq.heappop(numbers)
            if shrink < k:
                i = max(i, shrink + 1)
            elif shrink > k:
                j = min(j, shrink - 1)
            else:
                result = max(result, nums[k])
                return result

        return result
