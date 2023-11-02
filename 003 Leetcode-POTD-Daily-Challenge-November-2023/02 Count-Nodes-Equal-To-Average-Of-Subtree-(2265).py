# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        results = 0

        def go(node):
            if node is None:
                return 0, 0
            nonlocal results
            leftCount, leftSum = go(node.left)
            rightCount, rightSum = go(node.right)
            totalSum = node.val + (leftSum + rightSum)
            totalCount = 1 + (leftCount + rightCount)
            if (totalSum // totalCount) == node.val:
                results += 1
            return totalCount,totalSum

        go(root)
        return results
