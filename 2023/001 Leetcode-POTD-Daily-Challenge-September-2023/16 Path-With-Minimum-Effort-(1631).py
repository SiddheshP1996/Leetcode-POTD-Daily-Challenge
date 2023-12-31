import collections


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        left, right = 0, 10 ** 6

        # Define possible directions: up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while left < right:
            mid = (left + right) // 2
            visited = [[False] * cols for _ in range(rows)]
            queue = collections.deque([(0, 0)])
            visited[0][0] = True

            while queue:
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and abs(
                            heights[x][y] - heights[nx][ny]) <= mid:
                        queue.append((nx, ny))
                        visited[nx][ny] = True

            if visited[rows - 1][cols - 1]:
                # If it's possible to reach the bottom-right cell with the current effort, decrease the effort
                right = mid
            else:
                # Otherwise, increase the effort
                left = mid + 1

        return left
