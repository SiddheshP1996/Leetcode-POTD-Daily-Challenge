# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        result = []

        if root is None:
            return result

        q.append(root)
        INF = (10 ** 20)

        while len(q) > 0:
            size = len(q)
            maxLevel = -INF
            for _ in range(size):
                node = q.popleft()
                maxLevel = max(maxLevel, node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            result.append(maxLevel)
        return result
