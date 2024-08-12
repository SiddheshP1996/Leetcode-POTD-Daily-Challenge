from sortedcontainers import SortedList

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nlist = SortedList([-x for x in nums])
        self.k = k

    def add(self, val: int) -> int:
        self.nlist.add(-val)
        if len(self.nlist) >= self.k:
            return -self.nlist[self.k - 1]
        return -self.nlist[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
