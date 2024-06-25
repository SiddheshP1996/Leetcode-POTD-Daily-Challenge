from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadEndSlot = set(deadends)
        queue = deque()
        queue.append(('0000', 0))
        visitedSlot = set('0000')

        while queue:
            currentString, currentSteps = queue.popleft()

            if currentString == target:
                return currentSteps

            if currentString in deadEndSlot:
                continue

            for i in range(4):
                digit = int(currentString[i])
                for dir in [1, -1]:
                    newDigit = (digit + dir) % 10

                    newString = currentString[:i] + str(newDigit) + currentString[i+1:]

                    if newString not in visitedSlot:
                        visitedSlot.add(newString)
                        queue.append((newString, currentSteps+1))

        return -1
