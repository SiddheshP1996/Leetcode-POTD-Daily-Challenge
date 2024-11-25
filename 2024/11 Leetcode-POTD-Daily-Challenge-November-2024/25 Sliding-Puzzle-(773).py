from collections import deque
from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        targetSquare = "123450"
        startSquare = ''.join(str(num) for row in board for num in row)
        
        neighbors = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
        }
        queue = deque([(startSquare, 0)])
        visitedSquare = set()
        visitedSquare.add(startSquare)
        
        while queue:
            state, moves = queue.popleft()            
            if state == targetSquare:
                return moves
            
            indexZero = state.index('0')            
            for neighbor in neighbors[indexZero]:
                newState = list(state)
                newState[indexZero], newState[neighbor] = newState[neighbor], newState[indexZero]
                newStateString = ''.join(newState)
                
                if newStateString not in visitedSquare:
                    visitedSquare.add(newStateString)
                    queue.append((newStateString, moves + 1))
        
        return -1
