import collections

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def window(nums, k):
            leftSideNum = 0
            rightSideNum = 0

            result = 0
            numSet = set()
            hashMap = collections.Counter()

            while rightSideNum < len(nums):
                numSet.add(nums[rightSideNum])
                hashMap[nums[rightSideNum]] += 1

                while len(numSet) > k:
                    hashMap[nums[leftSideNum]] -= 1
                    if hashMap[nums[leftSideNum]] == 0:
                        numSet.remove(nums[leftSideNum])
                    leftSideNum += 1

                result += (rightSideNum - leftSideNum + 1)

                rightSideNum += 1
            return result
        return window(nums, k) - window(nums, k - 1)
