"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        currentHead = head
        previousHead = None
        while currentHead is not None:
            total = 0
            ahead = currentHead
            while ahead is not None:
                total += ahead.val
                if total == 0:
                    if previousHead is None:
                        return self.removeZeroSumSublists(ahead.next)
                    else:
                        previousHead.next = ahead.next
                        return self.removeZeroSumSublists(head)
                ahead = ahead.next
            previousHead = currentHead
            currentHead = currentHead.next
        return head
