class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        existingArrayNums = set()
        maximumFound = -1
        nums.sort()
        for n in nums:
            if n < 0:
                existingArrayNums.add(n)
            else:
                if -n in existingArrayNums:
                    maximumFound = n
        return maximumFound
