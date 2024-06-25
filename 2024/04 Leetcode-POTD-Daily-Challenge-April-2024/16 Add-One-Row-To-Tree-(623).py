"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        def execute(node, d):
            if node is None:
                return node
            if d == depth - 1:
                right = node.right
                left = node.left
                node.left = TreeNode(val, left)
                node.right = TreeNode(val, None, right)
            else:
                node.left = execute(node.left, d + 1)
                node.right = execute(node.right, d + 1)
            return node

        return execute(root, 1)
