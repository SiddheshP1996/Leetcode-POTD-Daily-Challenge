"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parents = {}
        start = None

        def execute(node, p):
            if node is None:
                return
            nonlocal start
            
            if node.val == startValue:
                start = node
            parents[node] = p
            
            execute(node.left, node)
            execute(node.right, node)

        execute(root, None)
        result = []

        def find(node, parentNode, currentNode):
            if node is None:
                return ""
            
            if node.val == destValue:
                return "".join(currentNode)
            
            if parents[node] != parentNode:
                currentNode.append('U')
                resultHere = find(parents[node], node, currentNode)
                
                if resultHere != "":
                    return resultHere
                currentNode.pop()
                
            if node.left != parentNode:
                currentNode.append('L')
                resultHere = find(node.left, node, currentNode)
                
                if resultHere != "":
                    return resultHere
                currentNode.pop()
                
            if node.right != parentNode:
                currentNode.append('R')
                resultHere = find(node.right, node, currentNode)
                if resultHere != "":
                    return resultHere
                currentNode.pop()
            return ""

        return find(start, None, [])
