# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        list = []

        def flatten(ni):
            if ni.isInteger():
                return list.append(ni.getInteger())
            arr = ni.getList()
            N = len(arr)
            if N == 0:
                return
            for i in range(N):
                if arr[i].isInteger():
                    list.append(arr[i].getInteger())
                else:
                    flatten(arr[i])

        for el in nestedList:
            flatten(el)
        self.list = collections.deque(list)

    def next(self) -> int:
        return self.list.popleft()

    def hasNext(self) -> bool:
        return len(self.list) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
