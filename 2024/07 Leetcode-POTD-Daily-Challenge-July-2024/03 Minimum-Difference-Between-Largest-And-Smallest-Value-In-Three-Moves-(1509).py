class Solution:
    def minDifference(self, nums: List[int]) -> int:
        smallest = nsmallest(4, nums)
        largest = nlargest(4, nums)
        return min(x - y for x, y in zip(largest, reversed(smallest)))
