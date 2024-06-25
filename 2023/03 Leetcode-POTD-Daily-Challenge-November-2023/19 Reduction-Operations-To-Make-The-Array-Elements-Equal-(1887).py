import collections


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        counterOfOperations = collections.defaultdict(int)

        n = len(nums)

        for i in range(n):
            counterOfOperations[nums[i]] += 1

        distinct = list(counterOfOperations.keys())
        distinct.sort()
        results = 0

        while len(distinct) > 1:
            number = distinct.pop()
            results += counterOfOperations[number]
            nextNumber = distinct[-1]
            counterOfOperations[nextNumber] += counterOfOperations[number]
        return results
