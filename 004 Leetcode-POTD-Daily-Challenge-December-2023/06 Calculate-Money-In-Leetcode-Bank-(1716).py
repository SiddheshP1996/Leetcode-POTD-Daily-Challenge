class Solution:
    def totalMoney(self, n: int) -> int:
        if n == 0:
            return 0
        result = [0] * n
        result[0] = 1

        for i in range(1, n):
            if i < 7:
                result[i] = result[i - 1] + 1
            else:
                result[i] = result[i - 7] + 1
        return sum(result)
    