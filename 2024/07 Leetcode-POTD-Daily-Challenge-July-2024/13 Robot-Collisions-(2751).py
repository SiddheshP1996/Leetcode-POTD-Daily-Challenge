class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        
        stack = []
        results = [None] * len(positions)
        
        for position, health, direction, index in robots:
            if direction == 'R':
                stack.append((position, health, direction, index))
            else:
                while stack and health > 0:
                    rightPosition, rightHealth, rightDirection, rightIndex = stack[-1]
                    if rightHealth < health:
                        health -= 1
                        stack.pop()
                    elif rightHealth > health:
                        stack[-1] = (rightPosition, rightHealth - 1, rightDirection, rightIndex)
                        health = 0
                    else:
                        stack.pop()
                        health = 0
                
                if health > 0:
                    results[index] = health
        
        while stack:
            position, health, direction, index = stack.pop()
            results[index] = health
        
        return [health for health in results if health is not None]
