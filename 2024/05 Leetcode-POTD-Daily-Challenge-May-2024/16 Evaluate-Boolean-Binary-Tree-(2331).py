"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def execute(node):
            if node.right is None and node.left is None:
                return node.val == 1
            leftBoolean = execute(node.left)
            rightBoolean = execute(node.right)
            if node.val == 2:
                return leftBoolean or rightBoolean
            return leftBoolean and rightBoolean

        return execute(root)
