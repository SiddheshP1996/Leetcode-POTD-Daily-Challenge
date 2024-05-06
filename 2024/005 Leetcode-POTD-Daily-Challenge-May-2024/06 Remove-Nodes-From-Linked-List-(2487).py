from collections import deque

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        monoQueue = deque()
        currentNode = head
        while currentNode is not None:
            while len(monoQueue) > 0 and currentNode.val > monoQueue[-1].val:
                monoQueue.pop()
            monoQueue.append(currentNode)
            currentNode = currentNode.next
        monoQueue.append(None)
        newHeadNode = monoQueue.popleft()
        currentNode = newHeadNode
        while currentNode is not None:
            currentNode.next = monoQueue.popleft()
            currentNode = currentNode.next
        return newHeadNode
