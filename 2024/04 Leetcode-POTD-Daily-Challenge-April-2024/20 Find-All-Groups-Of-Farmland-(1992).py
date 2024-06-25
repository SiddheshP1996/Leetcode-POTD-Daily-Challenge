class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        farmlandKaArray = []
        
        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1 and (i == 0 or land[i - 1][j] == 0) and (j == 0 or land[i][j - 1] == 0):
                    bottomWalaRow = i
                    rightWalaColumn = j

                    while bottomWalaRow + 1 < rows and land[bottomWalaRow + 1][j] == 1:
                        bottomWalaRow += 1
                    while rightWalaColumn + 1 < cols and land[i][rightWalaColumn + 1] == 1:
                        rightWalaColumn += 1

                    farmlandKaArray.append([i, j, bottomWalaRow, rightWalaColumn])
                    
        return farmlandKaArray
