# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # after exiting the while loop
        # L is the minimal index satisfying the condition function
        def binary_search(L, R, conditon):
            while L < R:
                mid = L + (R - L) // 2
                if conditon(mid):
                    R = mid
                else:
                    L = mid + 1
            return L

        cache = {}  # cache for performance

        def get(k):
            if k in cache:
                return cache[k]
            cache[k] = mountain_arr.get(k)
            return cache[k]

        length = mountain_arr.length()
        peakIdx = binary_search(0, length - 1, lambda k: get(k - 1) > get(k))
        findInLeft = binary_search(0, peakIdx, lambda k: get(k) >= target)
        if get(findInLeft) == target:
            return findInLeft
        findInRight = binary_search(peakIdx, length - 1, lambda k: get(k) <= target)
        return findInRight if get(findInRight) == target else -1
