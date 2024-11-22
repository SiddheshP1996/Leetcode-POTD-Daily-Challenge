class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patternCount = {}
        
        for row in matrix:
            normalized = tuple(cell if row[0] == 0 else 1 - cell for cell in row)
            
            if normalized not in patternCount:
                patternCount[normalized] = 0
            patternCount[normalized] += 1
        
        return max(patternCount.values())
