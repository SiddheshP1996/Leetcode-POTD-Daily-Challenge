"""
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def goTraverseTree(node, result):
            if node is None:
                return
            result.append(str(node.val))
            if node.left is not None or node.right is not None:
                result.append('(')
                goTraverseTree(node.left, result)
                result.append(')')
            if node.right is not None:
                result.append('(')
                goTraverseTree(node.right, result)
                result.append(')')
            return result

        return "".join(goTraverseTree(root, []))
