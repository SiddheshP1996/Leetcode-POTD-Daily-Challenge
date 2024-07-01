class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        def execute(i):
            if i >= n - 2:
                return False
            for j in range(i, i + 3):
                if arr[j] % 2 == 0:
                    return execute(i + 1)
            return True
        return execute(0)
