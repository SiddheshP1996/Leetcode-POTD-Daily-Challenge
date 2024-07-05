"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head is None:
            return [-1,-1]
        indexes = []
        index = 0
        previousIndex = head
        currrentIndex = head.next
        if currrentIndex is None or currrentIndex.next is None:
            return [-1,-1]
        next = currrentIndex.next

        while next is not None:
            if  currrentIndex.val < previousIndex.val and currrentIndex.val < next.val:
                indexes.append(index)
            elif currrentIndex.val > previousIndex.val and currrentIndex.val > next.val:
                indexes.append(index)
            previousIndex = currrentIndex
            currrentIndex = next
            next = next.next
            index += 1
        n = len(indexes)
        if n < 2:
            return [-1, -1]
        INF = 10 ** 20
        result = [INF,-1]
        for i in range(1, n):
            result[0] = min(result[0], (indexes[i] - indexes[i-1]  ) )
            result[1] = max(result[1], (indexes[i] - indexes[0]  ))
        return result
