"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1 for _ in range(n)] for _ in range(m)]
        if head is None:
            return result
        
        DIRECTIONS = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]

        def isValidIndex(i, j):
            return i >= 0 and i < m and j >= 0 and j < n and result[i][j] == -1

        def execute(i, j, direction, current):
            if current is None:
                return True
            
            if not isValidIndex(i, j):
                return False
            
            result[i][j] = current.val
            directionY, directionX = DIRECTIONS[direction]
            validIndex = execute(i + directionY, j + directionX, direction, current.next)
            
            while not validIndex:
                direction = (direction + 1) % (len(DIRECTIONS))
                directionY, directionX = DIRECTIONS[direction]
                validIndex = execute(i + directionY, j + directionX, direction, current.next)
            return validIndex

        execute(0, 0, 0, head)
        return result
