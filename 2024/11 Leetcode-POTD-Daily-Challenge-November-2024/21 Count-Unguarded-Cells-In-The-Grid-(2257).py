class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        
        for rows, cols in guards:
            grid[rows][cols] = 1
            
        for rows, cols in walls:
            grid[rows][cols] = 1
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for rows, cols in guards:
            for rowDirection, colDirection in directions:
                newRow, newCol = rows + rowDirection, cols + colDirection
                while 0 <= newRow < m and 0 <= newCol < n:
                    if grid[newRow][newCol] == 1: 
                        break
                    if grid[newRow][newCol] == 0:
                        grid[newRow][newCol] = 2
                    newRow += rowDirection
                    newCol += colDirection
        
        unguardedCount = sum(1 for rows in range(m) for cols in range(n) if grid[rows][cols] == 0)
        
        return unguardedCount
