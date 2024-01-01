class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        g.sort(reverse=True)
        s.sort()

        n = len(g)

        for i in range(n):
            if len(s) == 0:
                break
            if s[-1] < g[i]:
                continue
            result += 1
            s.pop()
        return result
