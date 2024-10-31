from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])
        memoryLen = {}

        def executer(currentRobot, currentFactory, usedCapacity):
            if currentRobot == len(robot):
                return 0
            
            if currentFactory == len(factory):
                return float('inf')

            key = (currentRobot, currentFactory, usedCapacity)
            if key in memoryLen:
                return memoryLen[key]

            minDist = executer(currentRobot, currentFactory + 1, 0)
            position, capacity = factory[currentFactory]
            
            if usedCapacity < capacity:
                robotDistance = abs(robot[currentRobot] - position)
                execute = executer(currentRobot + 1, currentFactory, usedCapacity + 1)
                minDist = min(minDist, robotDistance + execute)

            memoryLen[key] = minDist
            return minDist

        return executer(0, 0, 0)
