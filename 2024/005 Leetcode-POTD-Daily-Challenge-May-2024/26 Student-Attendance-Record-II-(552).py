class Solution:
    def checkRecord(self, n: int) -> int:
        mod = ((10 ** 9) + 7)

        cache = [[[-1 for _ in range(2)] for _ in range(3)] for _ in range(n)]

        def execute(present, late, absent):
            if late >= 3:
                return 0
            if absent >= 2:
                return 0
            if present == n:
                return 1
            if cache[present][late][absent] >= 0:
                return cache[present][late][absent]
            result = 0
            result += (execute(present + 1, 0, absent) % mod)  # Present
            result += (execute(present + 1, late + 1, absent) % mod)  # Late
            result += (execute(present + 1, 0, absent + 1) % mod)  # Late
            cache[present][late][absent] = result
            return result % mod

        return execute(0, 0, 0)
