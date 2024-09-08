"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        linkedListArray = []
        currentNode = head
        
        while currentNode is not None:
            linkedListArray.append(currentNode.val)
            currentNode = currentNode.next
            
        roots = [ListNode(-1) for _ in range(k)]
        result = [roots[i] for i in range(k)]
        sizes = [0] * k
        avg = math.floor(len(linkedListArray) / k)
        mod = len(linkedListArray) % k
        index = 0
        targetRoot = avg
        if mod > 0:
            targetRoot += 1
            mod -= 1
            
        for element in linkedListArray:
            result[index].next = ListNode(element)
            result[index] = result[index].next
            sizes[index] += 1
            
            if sizes[index] == targetRoot:
                index += 1
                targetRoot = avg
                
                if mod > 0:
                    targetRoot += 1
                    mod -= 1
                    
        for i in range(k):
            result[i] = roots[i].next

        return result
