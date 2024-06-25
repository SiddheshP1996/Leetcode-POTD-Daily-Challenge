class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrixOfArray = []
        for i in range(0,len(matrix[0])):
            arrayInMatrix = []
            for j in range(0,len(matrix)):
                arrayInMatrix.append(matrix[j][i])
            matrixOfArray.append(arrayInMatrix)
        return matrixOfArray
