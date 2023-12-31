class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        n = nums

        n.sort()
        leftNumber = rightNumber = results = totalOfAll = 0

        while rightNumber < len(n):
            totalOfAll += n[rightNumber]

            while (n[rightNumber] * ((rightNumber - leftNumber) + 1)) > (totalOfAll + k):
                totalOfAll -= n[leftNumber]
                leftNumber += 1

            results = max(results, ((rightNumber - leftNumber) + 1))
            rightNumber += 1

        return results
    