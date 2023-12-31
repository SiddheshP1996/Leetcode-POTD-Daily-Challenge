# Solution No 1

from typing import List

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = ((10**9) + 7)
        revDifferentFrequency = {}
        nicePairsCounter = 0

        for num in nums:
            # Calculate the difference between the number and its reverse
            rev_diff = num - int(str(num)[::-1])

            # Increment the frequency of the difference in the dictionary
            revDifferentFrequency[rev_diff] = revDifferentFrequency.get(rev_diff, 0) + 1

            # Add the frequency to the nicePairsCounter
            nicePairsCounter = (nicePairsCounter + revDifferentFrequency[rev_diff] - 1) % mod

        return nicePairsCounter

# Solution No 2


"""
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = ((10**9) + 7)
        revDifferentFrequency = {}
        nicePairsCounter = 0

        for num in nums:
            # Calculate the difference between the number and its reverse
            rev_diff = num - int(str(num)[::-1])

            # Increment the frequency of the difference in the dictionary
            revDifferentFrequency[rev_diff] = revDifferentFrequency.get(rev_diff, 0) + 1

            # Add the frequency to the nicePairsCounter
            nicePairsCounter = (nicePairsCounter + revDifferentFrequency[rev_diff] - 1) % mod

        return nicePairsCounter
"""
