class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            if i % 2 == 0:
                ans.append(bin(i).count('1'))
            else:
                ans.append(ans[i >> 1] + 1)
        return ans
