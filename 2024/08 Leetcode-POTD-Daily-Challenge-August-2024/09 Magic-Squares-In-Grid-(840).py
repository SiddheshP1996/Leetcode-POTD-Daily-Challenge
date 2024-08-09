class Solution:
    def checkDiagonals(self, matrix):
        n = int(len(matrix) / 2) + 1
        front = [] 
        back = []
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    front.extend([matrix[i][j], matrix[n - i][n - j]])
                    back.extend([matrix[i][n - j], matrix[n - j][i]])
                    
        if sum(front[:len(matrix)]) == sum(back[:len(matrix)]):
            return True
        return False

    def checkRows(self, matrix):
        topRow = sum(matrix[0])
        middleRow = sum(matrix[1])
        bottomRow = sum(matrix[2])
        
        if topRow == middleRow == bottomRow:
            return True
        return False
        
    def checkColumns(self, matrix):
        rightColumn = 0
        middleColumn = 0
        leftColumn = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                rightColumn += matrix[i][0]
                middleColumn += matrix[i][1]
                leftColumn += matrix[i][2]
                
        if rightColumn == middleColumn == leftColumn:
            return True
        return False
    
    def checkMatrix(self, matrix):
        numberSet = set()
        for i in matrix:
            for j in range(len(i)):
                if i[j] < 10 and i[j] > 0:
                    numberSet.add(i[j])
                    
        if len(numberSet) != 9:
            return False
        return True
    
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid) - 2):
            for j in range(0, len(grid[0]) - 2):
                subGrid = grid[i:i + 3]
                for k in range(len(subGrid)):
                    subGrid[k] = subGrid[k][j:j + 3]
                    
                if self.checkMatrix(subGrid) is False:
                    continue
                else:
                    if self.checkDiagonals(subGrid) and \
                        self.checkColumns(subGrid) and \
                            self.checkRows(subGrid):
                                result += 1
        return result
