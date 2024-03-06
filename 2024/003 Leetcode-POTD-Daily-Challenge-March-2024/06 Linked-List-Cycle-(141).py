"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next

        while slow is not None and fast is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next
        return False
