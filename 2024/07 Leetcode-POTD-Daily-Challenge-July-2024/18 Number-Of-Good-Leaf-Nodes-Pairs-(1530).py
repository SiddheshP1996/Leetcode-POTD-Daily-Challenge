"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count = 0
        MAX_DISTANCE = 10

        def dfs(node: TreeNode) -> List[int]:
            if not node:
                return [0] * (MAX_DISTANCE + 1)
            
            if not node.left and not node.right:
                result = [0] * (MAX_DISTANCE + 1)
                result[1] = 1
                return result
            
            leftNode = dfs(node.left)
            rightNode = dfs(node.right)
            
            for i in range(1, distance + 1):
                for j in range(1, distance - i + 1):
                    self.count += leftNode[i] * rightNode[j]
            
            result = [0] * (MAX_DISTANCE + 1)
            for i in range(1, MAX_DISTANCE):
                result[i + 1] = leftNode[i] + rightNode[i]
            
            return result

        dfs(root)
        return self.count
