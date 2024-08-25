"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def postorder(self, node, travelToPost):
        if node is None:
            return
        
        self.postorder(node.left, travelToPost)
        self.postorder(node.right, travelToPost)
        travelToPost.append(node.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        travelToPost = []
        self.postorder(root, travelToPost)
        return travelToPost
