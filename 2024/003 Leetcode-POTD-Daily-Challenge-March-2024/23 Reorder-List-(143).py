"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None

        def execute_second_half(head):
            slow = head
            fast = head.next
            
            while slow is not None and fast is not None and fast.next is not None and fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverse_ll(head):
            if head is None:
                return None
            previousPointer = None
            pointerOne = head
            pointerTwo = head.next
            
            while pointerOne is not None:
                pointerOne.next = previousPointer
                previousPointer = pointerOne
                pointerOne = pointerTwo
                
                if pointerTwo is not None:
                    pointerTwo = pointerTwo.next
            return previousPointer


        first_half_tail = execute_second_half(head)
        second_half_head = first_half_tail.next
        first_half_tail.next = None
        second_half_head = reverse_ll(second_half_head)

        currentHead = head
        second_half_currentHead = second_half_head
        
        while currentHead is not None and second_half_currentHead is not None:
            backup_first = currentHead.next
            backup_second = second_half_currentHead.next
            to_be_inserted = second_half_currentHead
            to_be_inserted.next = None
            currentHead.next = to_be_inserted
            currentHead = currentHead.next
            currentHead.next = backup_first
            currentHead = currentHead.next
            second_half_currentHead = backup_second
            
        if second_half_currentHead is not None:
            currentHead = head
            
            while currentHead.next is not None:
                currentHead = currentHead.next
            currentHead.next = second_half_currentHead
