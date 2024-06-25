"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        previousNode = None
        while node is not None:
            if node.next is None:
                previousNode.next = None
                break
            node.val = node.next.val
            previousNode = node
            node = node.next
