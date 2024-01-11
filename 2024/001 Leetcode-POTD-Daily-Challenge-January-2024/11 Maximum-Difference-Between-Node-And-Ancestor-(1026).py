"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, minimum, maximum):
            if not node:
                return 0
            nodeMaxValue = max(node.val, maximum)
            nodeMinValue = min(node.val, minimum)
            return max(dfs(node.left, nodeMinValue, nodeMaxValue), dfs(node.right, nodeMinValue, nodeMaxValue), abs(node.val - minimum), abs(node.val - maximum))
        return dfs(root, root.val, root.val)
