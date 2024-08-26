"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        selfRootArray = []
        listOfRoot =[]
        selfRootArray.append(root)
        if not root:
            return
        while(selfRootArray):
            temp = selfRootArray.pop()
            listOfRoot .append(temp.val)
            for i in temp.children:
                selfRootArray.append(i)
        return listOfRoot [::-1]
