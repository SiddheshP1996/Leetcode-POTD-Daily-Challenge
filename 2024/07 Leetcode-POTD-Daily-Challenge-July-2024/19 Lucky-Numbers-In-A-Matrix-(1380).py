class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rowMinimum = {min(row) for row in matrix}
        columnMaximum = {max(column) for column in zip(*matrix)}
        return list(rowMinimum & columnMaximum)
