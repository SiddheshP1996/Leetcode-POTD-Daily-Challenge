class Solution:
    def minSteps(self, s: str, t: str) -> int:
        t = collections.Counter(t)
        n = len(s)
        def execute_minSteps(i):
            if i == n:
                return sum(t.values())
            c = s[i]
            if t[c] > 0:
                t[c] -= 1
                return execute_minSteps(i + 1)
            return execute_minSteps(i + 1)

        return execute_minSteps(0)
