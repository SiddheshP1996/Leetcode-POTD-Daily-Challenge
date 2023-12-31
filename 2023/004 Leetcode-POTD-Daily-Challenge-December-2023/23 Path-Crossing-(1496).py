class Solution:
    def isPathCrossing(self, path: str) -> bool:
        verticalPath = 0
        horizontalPath = 0

        pathHistory = set()
        pathHistory.add((verticalPath, horizontalPath))

        for c in path:
            if c == 'N':
                verticalPath += 1
            elif c == 'S':
                verticalPath -= 1
            elif c == 'W':
                horizontalPath += 1
            elif c == 'E':
                horizontalPath -= 1
            if (verticalPath, horizontalPath) in pathHistory:
                return True
            pathHistory.add((verticalPath, horizontalPath))
        return False
