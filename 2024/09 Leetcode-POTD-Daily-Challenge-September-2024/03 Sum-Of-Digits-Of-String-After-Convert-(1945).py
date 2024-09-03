class Solution:
    def getLucky(self, s: str, k: int) -> int:
        number = 0
        for c in s:
            x = ord(c) - 96
            q, r = divmod(x, 10)
            number += q + r
        k -= 1
        x = number
        for _ in range(k, 0, -1):
            number = 0
            while x > 0:
                q, r = divmod(x, 10)
                number += r
                x = q
            x = number
            if x < 10:break
        return number
