class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        obstacle = [[float('inf')]*col for _ in range(row)]
        q = deque([(0, 0, 0)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        obstacle[0][0] = 0
        while q:
            obs, x, y = q.popleft()
            for dirX, dirY in directions:
                newX, newY = x + dirX, y + dirY
                if newX < 0 or newY < 0 or newX >= row or newY >= col:
                    continue
                if obstacle[newX][newY] == float('inf'):
                    if grid[newX][newY] == 1:
                        obstacle[newX][newY] = obs + 1
                        q.append((obs + 1, newX, newY))
                    else:
                        obstacle[newX][newY] = obs
                        q.appendleft((obs, newX, newY))
        return obstacle[row - 1][col - 1]
