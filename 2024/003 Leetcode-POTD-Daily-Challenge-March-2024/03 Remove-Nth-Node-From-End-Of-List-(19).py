"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        previousHead = None
        currentHead = head
        tailEnd = head
        for tail in range(n):
            tailEnd = tailEnd.next
        if tailEnd is None:
            return head.next
        while currentHead is not None:
            if tailEnd is None:
                previousHead.next = currentHead.next
                currentHead.next = None
                break
            previousHead = currentHead
            currentHead = currentHead.next
            tailEnd = tailEnd.next
        return head
