from heapq import heappop, heappush

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        gridM, gridN = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        visited = [[False] * gridN for _ in range(gridM)]
        heap = [(0, 0, 0)]
        while heap:
            time, row, col = heappop(heap)
            if row == gridM - 1 and col == gridN - 1:
                return time
            if visited[row][col]:
                continue
            visited[row][col] = True
            for dirRow, dirCol in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                newRow, newCol = row + dirRow, col + dirCol
                if newRow < 0 or newRow >= gridM or newCol < 0 or newCol >= gridN or visited[newRow][newCol]:
                    continue
                wait = (grid[newRow][newCol] - time) % 2 == 0
                newTime = max(grid[newRow][newCol] + wait, time + 1)
                heappush(heap, (newTime, newRow, newCol))
        return -1
