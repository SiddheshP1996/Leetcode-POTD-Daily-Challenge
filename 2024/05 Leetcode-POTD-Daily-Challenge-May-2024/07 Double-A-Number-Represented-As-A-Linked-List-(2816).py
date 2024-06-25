"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(1000000000)
        currentNode = head
        number = 0
        while currentNode is not None:
            number = (number * 10) + currentNode.val
            currentNode = currentNode.next
        number *= 2
        newHeadNode = ListNode(-1)
        currentNode = newHeadNode
        for d in str(number):
            currentNode.next = ListNode(int(d))
            currentNode = currentNode.next
        return newHeadNode.next
