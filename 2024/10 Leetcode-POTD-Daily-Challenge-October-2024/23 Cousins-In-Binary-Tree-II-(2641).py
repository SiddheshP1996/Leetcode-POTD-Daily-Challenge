"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.depth_sum = []

        def dfsOne(node, nodeDepth):
            if not node: return

            if nodeDepth >= len(self.depth_sum):
                self.depth_sum.append(node.val)
            else:
                self.depth_sum[nodeDepth] += node.val

            dfsOne(node.left, nodeDepth + 1)
            dfsOne(node.right, nodeDepth + 1)

        def dfsTwo(node, val, nodeDepth):
            if not node: return
            node.val = val

            cousin = self.depth_sum[nodeDepth + 1] if nodeDepth + 1 < len(self.depth_sum) else 0
            cousin -= (node.left.val if node.left else 0)
            cousin -= (node.right.val if node.right else 0)

            if node.left:
                dfsTwo(node.left, cousin, nodeDepth + 1)
            if node.right:
                dfsTwo(node.right, cousin, nodeDepth + 1)

        dfsOne(root, 0)
        dfsTwo(root, 0, 0)
        return root
