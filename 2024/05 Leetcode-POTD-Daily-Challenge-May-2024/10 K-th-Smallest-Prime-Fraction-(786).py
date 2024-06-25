from heapq import heappop, heapify

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fraction = []
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                fraction.append((arr[i] / arr[j], arr[i], arr[j]))
        heapify(fraction)
        result = []
        for i in range(k):
            _, a, b = heappop(fraction)
            result = [a, b]
        return result
