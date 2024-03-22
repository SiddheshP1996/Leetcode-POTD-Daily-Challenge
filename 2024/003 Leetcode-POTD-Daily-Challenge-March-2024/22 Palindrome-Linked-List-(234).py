"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def execute(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        result = self.execute(head.next) and head.val == self.curr.val
        self.curr = self.curr.next
        return result

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.curr = head
        return self.execute(head)
