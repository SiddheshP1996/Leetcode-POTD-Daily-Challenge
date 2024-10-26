"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        result = defaultdict(int)

        def dfs(root, height, maxHeight):
            if not root: return maxHeight
            result[root.val] = max(result[root.val], maxHeight)
            root.left, root.right = root.right, root.left
            return dfs(root.right, height + 1, dfs(root.left, height + 1, max(maxHeight, height)))

        dfs(root, 0, 0)
        dfs(root, 0, 0)
        return [result[query] for query in queries]
