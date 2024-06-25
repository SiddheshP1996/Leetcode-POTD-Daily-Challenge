class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        for power_of_n in bin(n)[2::]:
            if power_of_n == "1":
                count += 1
        return count == 1 and n > 0
