"""
Solution 1
mod = 10**9 + 7
class Solution:
    def countOrders(self, n: int) -> int:
        result = 1
        for i in range(2, n + 1):
            result = ((result * (2 * i - 1) * i) % (mod))
        return result
"""

"""
Solution 2
"""

mod = 10 ** 9 + 7


class Solution:
    def countOrders(self, n: int) -> int:
        return (math.factorial(2 * n) // 2 ** n) % mod
