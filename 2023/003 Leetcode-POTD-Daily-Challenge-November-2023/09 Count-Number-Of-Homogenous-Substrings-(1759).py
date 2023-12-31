class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = ((10 ** 9) + 7)

        def naturalSum(homosubstr):
            if homosubstr == 0:
                return 0
            return (homosubstr * (homosubstr + 1)) // 2

        N = len(s)
        results = 0
        lastBreak = 0
        for i in range(1, N):
            if s[i] == s[i - 1]:
                continue
            equal = i - lastBreak
            results = ((results % mod) + (naturalSum(equal) % mod)) % mod
            lastBreak = i
        equal = N - lastBreak
        results = ((results % mod) + (naturalSum(equal) % mod)) % mod
        return results % mod
