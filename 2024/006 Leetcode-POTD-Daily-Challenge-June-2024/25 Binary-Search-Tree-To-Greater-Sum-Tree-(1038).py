"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if not root: return
            helper(root.right)
            total[0] += root.val
            root.val = total[0]
            helper(root.left)
        total = [0]
        helper(root)
        return root
