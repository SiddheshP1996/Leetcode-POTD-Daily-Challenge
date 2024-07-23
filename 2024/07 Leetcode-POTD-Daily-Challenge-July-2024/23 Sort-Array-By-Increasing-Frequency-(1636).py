from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = sorted(Counter(nums).items(), key=lambda x: (x[1], -x[0]))
        result = []
        for n, total in count:
            for _ in range(total):
                result.append(n)
        return result
