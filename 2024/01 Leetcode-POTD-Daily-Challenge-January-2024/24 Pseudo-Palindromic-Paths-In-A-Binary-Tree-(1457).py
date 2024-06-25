"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        result = 0

        def executePath(node, path):
            if node is None:
                return
            path[node.val] += 1
            if node.left is None and node.right is None:
                odd = 0
                for value in path.values():
                    if value % 2 != 0:
                        odd += 1
                    if odd > 1:
                        break
                if odd <= 1:
                    nonlocal result
                    result += 1
            else:
                executePath(node.right, path)
                executePath(node.left, path)
            path[node.val] -= 1

        executePath(root, collections.Counter())

        return result