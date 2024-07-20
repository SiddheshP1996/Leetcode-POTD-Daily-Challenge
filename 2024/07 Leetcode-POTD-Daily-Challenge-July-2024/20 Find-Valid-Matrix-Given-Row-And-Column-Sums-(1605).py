class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        columnSum = colSum
        rowSum = rowSum
        
        matrix = [[0]*len(columnSum) for i in range(len(rowSum))]
        rows = 0
        columns = 0
        while rows < len(rowSum) and columns < len(columnSum):
            matrix[rows][columns] = min(rowSum[rows], columnSum[columns])
            if rowSum[rows] == columnSum[columns]:
                rows += 1
                columns += 1
            elif rowSum[rows] > columnSum[columns]:
                rowSum[rows] -= columnSum[columns]
                columns += 1
            else:
                columnSum[columns] -= rowSum[rows]
                rows += 1

        return matrix
