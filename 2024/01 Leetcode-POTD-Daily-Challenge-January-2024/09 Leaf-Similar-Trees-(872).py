"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getSimilarLeafs(node, arr):
            if node is None:
                return arr
            if node.left is None and node.right is None:
                arr.append(node.val)
            getSimilarLeafs(node.left, arr)
            getSimilarLeafs(node.right, arr)
            return arr
        
        return getSimilarLeafs(root1,[]) == getSimilarLeafs(root2, [])
