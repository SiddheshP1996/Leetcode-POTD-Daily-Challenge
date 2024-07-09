class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        currentTime = customers[0][0]
        halt = 0
        for s, d in customers:
            currentTime = max(s, currentTime)
            currentTime += d
            halt += (currentTime - s)
        n = len(customers)
        return halt / n
