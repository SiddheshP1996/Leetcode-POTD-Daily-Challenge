class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        previousStack = [float('inf')] * n
        currentStack = [float('inf')] * n
        for day in range(d):
            presentStack = []
            for i in range(day, n):
                if i == 0:
                    currentStack[i] = jobDifficulty[0]
                else:
                    currentStack[i] = previousStack[i - 1] + jobDifficulty[i]
                while presentStack and jobDifficulty[presentStack[-1]] <= jobDifficulty[i]:
                    j = presentStack.pop()
                    currentStack[i] = min(currentStack[i], currentStack[j] + jobDifficulty[i] - jobDifficulty[j])
                if presentStack:
                    currentStack[i] = min(currentStack[i], currentStack[presentStack[-1]])
                presentStack.append(i)
            previousStack, currentStack = currentStack, previousStack
        return previousStack[-1]
