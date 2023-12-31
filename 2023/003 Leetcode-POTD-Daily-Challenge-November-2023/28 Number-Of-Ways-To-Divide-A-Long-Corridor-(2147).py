class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = ((10 ** 9) + 7)
        x = 1  # 0 seat
        y = 0  # 1 seat
        z = 0  # 2 seats
        for characters in corridor:
            if characters == 'S':
                x, y, z = 0, x + z, y
            else:
                x, y, z = x + z, y, z
        return z % mod
