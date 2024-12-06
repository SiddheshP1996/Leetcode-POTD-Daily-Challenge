class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        bannedSet = set(banned)
        totalSum = 0
        count = 0

        for i in range(1, n + 1):
            if i in bannedSet:
                continue
            totalSum += i
            if totalSum > maxSum:
                break
            count += 1

        return count
