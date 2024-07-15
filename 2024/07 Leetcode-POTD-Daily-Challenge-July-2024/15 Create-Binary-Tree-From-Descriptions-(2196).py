"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        parents = {}
        
        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
                
            if isLeft == 1:
                if child in nodes:
                    nodes[parent].left = nodes[child]
                else:
                    nodes[parent].left = TreeNode(child)
                    nodes[child] = nodes[parent].left
            else:
                if child in nodes:
                    nodes[parent].right = nodes[child]
                else:
                    nodes[parent].right = TreeNode(child)
                    nodes[child] = nodes[parent].right
            parents[child] = parent
        root = None
        
        for nodeKey, node in nodes.items():
            if nodeKey not in parents:
                return node
        return root
