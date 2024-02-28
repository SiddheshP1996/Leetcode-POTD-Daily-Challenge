"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue, result = [], []
        queue.append(root)
        while queue:
            root_level = []
            for element in range(len(queue)):
                node = queue.pop(0)
                root_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if root_level: result.append(root_level)
        return result[-1][0]
