"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def longest_distance(node):
            if node is None:
                return 0
            nonlocal result

            left_distance = longest_distance(node.left)
            right_distance = longest_distance(node.right)
            result = max(result, left_distance + right_distance)
            return 1 + max(left_distance, right_distance)

        longest_distance(root)
        return result
