class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        guaranteed = 0
        for i in range(n):
            if grumpy[i] == 0:
                guaranteed += customers[i]
                customers[i] = 0

        bestStore = 0
        leftStore = 0
        rightStore = 0
        currentSum = 0
        while rightStore < n:
            currentSum += customers[rightStore]
            while (rightStore - leftStore + 1) > minutes:
                currentSum -= customers[leftStore]
                leftStore += 1
            bestStore = max(bestStore, currentSum)
            rightStore += 1
        return guaranteed + bestStore
