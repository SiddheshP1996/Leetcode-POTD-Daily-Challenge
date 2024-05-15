from heapq import heappush, heappop

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        distance = [[float('inf')] * n for _ in range(n)]
        queueStore = deque()

        for row in range(n):
            for column in range(n):
                if grid[row][column] == 1:
                    queueStore.append((row, column))
                    distance[row][column] = 0

        while queueStore:
            row, column = queueStore.popleft()
            for rowDirection, columnDirection in directions:
                newRow, newColumn = row + rowDirection, column + columnDirection
                if 0 <= newRow < n and 0 <= newColumn < n and distance[newRow][newColumn] == float('inf'):
                    distance[newRow][newColumn] = distance[row][column] + 1
                    queueStore.append((newRow, newColumn))

        heapMaximum = [(-distance[0][0], 0, 0)]
        maximumSafe = [[-1] * n for _ in range(n)]
        maximumSafe[0][0] = distance[0][0]

        while heapMaximum:
            direction, row, column = heappop(heapMaximum)
            direction = -direction
            if row == n - 1 and column == n - 1:
                return direction

            for rowDirection, columnDirection in directions:
                newRow, newColumn = row + rowDirection, column + columnDirection
                if 0 <= newRow < n and 0 <= newColumn < n:
                    newlySafe = min(direction, distance[newRow][newColumn])
                    if newlySafe > maximumSafe[newRow][newColumn]:
                        maximumSafe[newRow][newColumn] = newlySafe
                        heappush(heapMaximum, (-newlySafe, newRow, newColumn))

        return -1
