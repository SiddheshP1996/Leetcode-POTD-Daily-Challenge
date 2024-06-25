"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

from collections import defaultdict, deque

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        parents = {}
        levels = defaultdict(deque)
        enqueued = set()
        maximumLevel = 0

        def getParents(node, parent, level):
            if node is None:
                return
            nonlocal maximumLevel
            maximumLevel = max(maximumLevel, level)
            levels[level].append(node)
            parents[node] = parent
            getParents(node.left, node, level + 1)
            getParents(node.right, node, level + 1)

            return

        getParents(root, None, 0)
        result = 0
        for level in range(maximumLevel, -1, -1):
            queue = levels[level]
            while len(queue) > 0:
                size = len(queue)
                for _ in range(size):
                    node = queue.popleft()
                    parent = parents[node]
                    coins = node.val
                    if node.left is not None and node.left.val <= 0:
                        result += abs(node.left.val)
                        coins += node.left.val
                    if node.right is not None and node.right.val <= 0:
                        result += abs(node.right.val)
                        coins += node.right.val
                    if coins > 1:
                        node.val = 1
                        if parent is not None:
                            parent.val += (coins - 1)
                        result += (coins - 1)
                    elif coins <= 0:
                        node.val = coins - 1
                    else:
                        node.val = coins
        return result
