"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def execute(node):
            if node is None:
                return 0
            result = 0
            if node.left is not None:
                if node.left.left is None and node.left.right is None:
                    result = node.left.val
            return result + execute(node.right) + execute(node.left)
        return execute(root)
