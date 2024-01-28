class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        for row in matrix:
            for num in range(len(row) - 1):
                row[num + 1] += row[num]

        count = 0
        for target_cell in range(len(matrix)):
            for target_base in range(target_cell, -1, -1):
                if target_cell == target_base:
                    current_cell = matrix[target_cell][:]
                else:
                    current_cell = [current_cell[num] + matrix[target_base][num] for num in range(len(matrix[0]))]
                seen = {0: 1}
                for vacant_cell in current_cell:
                    if vacant_cell - target in seen:
                        count += seen[vacant_cell - target]
                    seen[vacant_cell] = seen.get(vacant_cell, 0) + 1
                    
        return count
