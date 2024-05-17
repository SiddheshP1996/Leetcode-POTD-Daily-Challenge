"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def execute(node):
            if node is None:
                return None
            node.left = execute(node.left)
            node.right = execute(node.right)
            if node.left is None and node.right is None and node.val == target:
                return None
            return node

        return execute(root)
