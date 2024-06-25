class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def execute(num):
            if num == 0:
                return 0
            if num == 1:
                return 1
            if num == 2:
                return 1
            return execute(num - 1) + execute(num - 2) + execute(num - 3)
        return execute(n)
