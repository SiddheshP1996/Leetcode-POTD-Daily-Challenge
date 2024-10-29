class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        gridWidth = len(grid[0])
        gridHeight = len(grid)
        for column in range(1, gridWidth):
            missed = 0
            for row in range(gridHeight):
                cellValue = grid[row][column]
                if not (cellValue > grid[row][column - 1] or 
                        (row > 0 and cellValue > grid[row - 1][column - 1]) or 
                        (row < gridHeight - 1 and cellValue > grid[row + 1][column - 1])):
                    grid[row][column] = float('inf')
                    missed += 1
                if missed == gridHeight:
                    return column - 1
        return gridWidth - 1
