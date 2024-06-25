"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        currentNode = head

        while currentNode:
            n += 1
            currentNode = currentNode.next

        size = n // k
        modulus = n % k
        ans = [size for _ in range(k)]

        for i in range(modulus):
            ans[i] += 1
        currentNode = head

        for i in range(k):
            if currentNode:
                pointer = currentNode
                for j in range(ans[i] - 1):
                    currentNode = currentNode.next
                temp = currentNode.next
                currentNode.next = None
                currentNode = temp
                ans[i] = pointer
            else:
                ans[i] = None
        return ans