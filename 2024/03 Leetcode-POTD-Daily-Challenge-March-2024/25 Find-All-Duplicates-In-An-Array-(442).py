class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mask = 0
        resultArray = []
        for n in nums:
            if (1 << n) & mask != 0:
                resultArray.append(n)
            mask |= (1 << n)
        return resultArray
