import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        def go(node):
            if node is None:
                return
            go(node.left)
            arr.append(node.val)
            go(node.right)

        go(root)
        count = collections.Counter(arr)
        modes = count.most_common()
        results = []
        maxFrequency = -1
        for val, count in modes:
            if count < maxFrequency:
                break
            maxFrequency = count
            results.append(val)
        return results
