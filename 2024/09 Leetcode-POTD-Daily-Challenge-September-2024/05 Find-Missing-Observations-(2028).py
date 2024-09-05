class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        totalSum = mean * (n + len(rolls))
        missingSum = totalSum - sum(rolls)
        baseValue = missingSum // n
        remainder = missingSum % n

        if baseValue <= 0 or baseValue > 6 or (baseValue == 6 and remainder > 0):
            return []

        result = [baseValue] * n
        for i in range(remainder):
            result[i] += 1
        return result
