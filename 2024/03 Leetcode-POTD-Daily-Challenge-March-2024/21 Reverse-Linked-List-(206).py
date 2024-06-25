"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        previousNode = None
        currentNode = head
        
        while currentNode is not None:
            pointer2 = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = pointer2
        
        return previousNode
