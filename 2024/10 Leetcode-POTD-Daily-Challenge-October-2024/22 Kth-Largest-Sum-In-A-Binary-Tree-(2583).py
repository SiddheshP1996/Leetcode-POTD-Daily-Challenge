"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        levelSums = []
        queue = deque([root])
        
        while queue:
            levelSize = len(queue)
            levelSum = 0
            
            for _ in range(levelSize):
                node = queue.popleft()
                levelSum += node.val
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
            
            levelSums.append(levelSum)
        
        levelSums.sort(reverse=True)
        
        if len(levelSums) < k:
            return -1
        
        return levelSums[k - 1]
