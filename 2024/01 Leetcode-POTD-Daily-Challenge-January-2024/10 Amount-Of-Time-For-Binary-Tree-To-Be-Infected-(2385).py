"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        result = 0
        def DFS(node, start):
            
            if node == None:
                return 0
            
            leftDepthSearch = DFS(node.left, start)
            rightDepthSearch = DFS(node.right, start)
            
            if node.val == start:
                Solution.result = max(leftDepthSearch, rightDepthSearch)
                return -1
            
            elif leftDepthSearch >= 0 and rightDepthSearch >= 0:
                return max(leftDepthSearch, rightDepthSearch) + 1
            
            Solution.result = max(Solution.result, abs(leftDepthSearch - rightDepthSearch))
            return min(leftDepthSearch, rightDepthSearch) - 1
        DFS(root, start)
        return Solution.result
