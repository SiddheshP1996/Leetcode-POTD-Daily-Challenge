# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        leftNode = ListNode()
        leftNode.next = head
        current = head
        for i in range(1, right):

            if i < left - 1:
                current = current.next

            elif i == left - 1:
                leftNode = current
                current = current.next

            else:
                nextNext = current.next.next
                current.next.next = leftNode.next
                leftNode.next = current.next
                current.next = nextNext

        if left > 1: return head
        return leftNode.next