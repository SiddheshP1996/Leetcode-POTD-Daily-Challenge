class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        mCellNumber, nCellNumber = len(img), len(img[0])
        result = [[0] * nCellNumber for _ in range(mCellNumber)]
        for i in range(mCellNumber):
            for j in range(nCellNumber):
                counterOfCell = 0
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < mCellNumber and 0 <= y < nCellNumber:
                            result[i][j] += img[x][y]
                            counterOfCell += 1
                result[i][j] //= counterOfCell
        return result
