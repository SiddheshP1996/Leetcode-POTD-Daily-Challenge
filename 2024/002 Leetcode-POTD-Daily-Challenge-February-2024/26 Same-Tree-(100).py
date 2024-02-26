"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def DFS(point1 , point2):
            if point1 == None and point2 == None:
                return True
            
            elif point1 == None or point2 == None:
                return False
            
            elif point1.val != point2.val:
                return False
            
            return DFS(point1.left , point2.left) and DFS(point1.right , point2.right)
        return DFS(p , q)
