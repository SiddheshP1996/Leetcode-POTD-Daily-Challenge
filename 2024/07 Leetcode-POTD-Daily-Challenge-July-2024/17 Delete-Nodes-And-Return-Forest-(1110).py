"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = set()
        toDelete = set(to_delete)

        def execute(node, nRoot, parent):
            if node is None:
                if nRoot is not None:
                    result.add(nRoot)
                return
            
            if node.val in toDelete:
                if parent is not None and node == parent.left:
                    parent.left = None
                    result.add(nRoot)
                elif parent is not None and node == parent.right:
                    parent.right = None
                    result.add(nRoot)
                execute(node.left, node.left, None)
                execute(node.right, node.right, None)
            else:
                execute(node.left, nRoot, node)
                execute(node.right, nRoot, node)

        execute(root, root, None)
        return result
