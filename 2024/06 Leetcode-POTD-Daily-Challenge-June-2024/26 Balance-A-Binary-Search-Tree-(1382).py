"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def execute(node, numberArray):
            if node is None:
                return numberArray
            execute(node.left, numberArray)
            numberArray.append(node.val)
            execute(node.right, numberArray)
            return numberArray

        numberArray = execute(root, [])
        newRoot = TreeNode(-1)
        n = len(numberArray)

        def divideAndConquer(node, leftBound, rightBound):
            if leftBound < 0 or rightBound >= n:
                return
            middle = (rightBound + leftBound) // 2
            if numberArray[middle] >= node.val:
                node.right = TreeNode(numberArray[middle])
                node = node.right
            else:
                node.left = TreeNode(numberArray[middle])
                node = node.left
            if middle - 1 >= leftBound:
                divideAndConquer(node, leftBound, middle - 1)
            if middle + 1 <= rightBound:
                divideAndConquer(node, middle + 1, rightBound)

        divideAndConquer(newRoot, 0, n - 1)
        return newRoot.right
