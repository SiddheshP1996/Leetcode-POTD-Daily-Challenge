class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        n = len(s)
        exponential = 0
        for i in range(n - 1, -1, -1):
            if s[i] == "1":
                num += 2 ** exponential
            exponential += 1

        def execute(number):
            if number == 1:
                return 0
            if number % 2 == 0:
                return 1 + execute(number // 2)
            return 1 + execute(number + 1)

        return execute(num)
