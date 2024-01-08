"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        arr = []
        def inOrderTravelsal(node):
            if node is None:
                return
            inOrderTravelsal(node.left)
            arr.append(node.val)
            inOrderTravelsal(node.right)

        inOrderTravelsal(root)
        n = len(arr)
        result = 0
        leftRootNode = 0
        rightRootNode = n - 1
        startPoint = -1
        while leftRootNode <= rightRootNode:
            middleRootNode = (leftRootNode + rightRootNode) // 2
            if arr[middleRootNode] == low:
                startPoint = middleRootNode
                break
            elif arr[middleRootNode] < low:
                leftRootNode = middleRootNode + 1
            else:
                rightRootNode = middleRootNode - 1

        for i in range(startPoint, n):
            result += arr[i]
            if arr[i] == high:
                break
        return result
