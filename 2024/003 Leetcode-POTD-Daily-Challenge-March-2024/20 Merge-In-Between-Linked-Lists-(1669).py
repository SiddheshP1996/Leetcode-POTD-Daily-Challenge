"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        currentList = list1
        athNodeCut = None
        bthNodeCut = None
        for _ in range(a-1):
            currentList = currentList.next
        athNodeCut = currentList
        currentList = list1
        for _ in range(b):
            currentList = currentList.next
        bthNodeCut = currentList
        athNodeCut.next = list2
        tailList = list2
        while tailList.next is not None:
            tailList = tailList.next
        tailList.next = bthNodeCut.next
        return list1
