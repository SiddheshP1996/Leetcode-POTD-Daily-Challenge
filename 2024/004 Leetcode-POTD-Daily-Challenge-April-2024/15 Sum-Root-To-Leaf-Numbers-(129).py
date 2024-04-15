"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
        
        def execute(node, currentNode):
            if node is None:
                return 0
            nonlocal result
            
            currentNode.append(str(node.val))
            if node.left is None and node.right is None:
                result += int("".join(currentNode))
                currentNode.pop()
                return 
            
            execute(node.left, currentNode)
            execute(node.right, currentNode)
            currentNode.pop()
        
        execute(root, [])
        return result
