class Solution:
    def pivotInteger(self, n: int) -> int:
        def naturalSum(k):
            if k == 0:
                return 0
            return (k * (k + 1)) // 2


        for i in range(n + 1):
            if naturalSum(i) == naturalSum(n) - naturalSum(i - 1):
                return i
        return -1
