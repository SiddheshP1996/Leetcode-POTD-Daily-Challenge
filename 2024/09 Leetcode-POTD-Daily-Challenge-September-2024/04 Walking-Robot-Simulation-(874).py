class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        observations = set(map(tuple, obstacles))
        x, y, dx, dy, result = 0, 0, 0, 1, 0

        for c in commands:
            if c < 0 :
                dx, dy = (dy, -dx) if c == -1 else (-dy, dx)  
    
            else:
                for _ in range(c):
                    if (x + dx, y + dy) in observations: break
                    x, y = x + dx, y + dy

            result = max(result, (x * x) + (y * y))

        return result
