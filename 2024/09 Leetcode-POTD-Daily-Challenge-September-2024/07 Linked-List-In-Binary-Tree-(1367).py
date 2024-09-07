"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def compareValues(listNode: ListNode, treeNode: TreeNode):
            if not listNode:
                return True
            
            if treeNode and listNode.val == treeNode.val:
                return (compareValues(listNode.next, treeNode.left) or \
                    compareValues(listNode.next, treeNode.right))
            return False

        row = {root}
        while row:
            nextRow = set()
            for node in row:
                if node.val == head.val and compareValues(head, node):
                    return True
                
                if node.left:
                    nextRow.add(node.left)
                    
                if node.right:
                    nextRow.add(node.right)
            row = nextRow

        return False
