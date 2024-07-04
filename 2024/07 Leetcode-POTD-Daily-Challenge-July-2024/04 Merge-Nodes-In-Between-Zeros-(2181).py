"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        node = head.next
        currentSum = 0
        result = []

        while node is not None:
            if node.val == 0:
                result.append(currentSum)
                currentSum = 0
            else:
                currentSum += node.val
            node = node.next
        
        newHead = ListNode(-1)
        node = newHead
        for a in result:
            node.next = ListNode(a)
            node = node.next
        
        return newHead.next
