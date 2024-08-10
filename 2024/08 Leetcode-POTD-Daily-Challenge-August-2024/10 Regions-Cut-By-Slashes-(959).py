class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        rows, columns = len(grid), len(grid[0])
        newRows, newColumns = rows * 3, columns * 3
        newGrid = [[0 for _ in range(newColumns)] for _ in range(newRows)]

        def transform(character, x, y):
            nonlocal newGrid

            if character == '/':
                newGrid[x][y + 2] = 1
                newGrid[x + 1][y + 1] = 1
                newGrid[x + 2][y] = 1
            
            if character == '\\':
                newGrid[x][y] = 1
                newGrid[x + 1][y + 1] = 1
                newGrid[x + 2][y + 2] = 1
        
        def floodFill(x, y):
            nonlocal newGrid

            if not (0 <= x < newRows and 0 <= y < newColumns):
                return
            
            if newGrid[x][y] == 1 or newGrid[x][y] == 2:
                return
            
            newGrid[x][y] = 2
            floodFill(x + 1, y)
            floodFill(x, y + 1)
            floodFill(x - 1, y)
            floodFill(x, y - 1)
        
        for i in range(rows):
            for j in range(columns):
                transform(grid[i][j], i * 3, j * 3)
        
        result = 0
        for i in range(newRows):
            for j in range(newColumns):
                if newGrid[i][j] == 0:
                    result += 1
                    floodFill(i, j)
        
        return result
