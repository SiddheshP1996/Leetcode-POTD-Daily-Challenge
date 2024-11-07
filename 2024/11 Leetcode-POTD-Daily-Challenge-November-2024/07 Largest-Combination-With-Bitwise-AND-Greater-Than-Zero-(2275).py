class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        largest = 0
        for i in range(24):
            largest = max(largest, sum((candidate >> i) & 1 for candidate in candidates))
        return largest
