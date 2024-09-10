"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = head
        nextHead = head.next
        
        while nextHead != None:
            newNode = ListNode(math.gcd(head.val, nextHead.val))
            head.next = newNode
            newNode.next = nextHead
            head = nextHead
            nextHead = nextHead.next
        
        return dummyHead
