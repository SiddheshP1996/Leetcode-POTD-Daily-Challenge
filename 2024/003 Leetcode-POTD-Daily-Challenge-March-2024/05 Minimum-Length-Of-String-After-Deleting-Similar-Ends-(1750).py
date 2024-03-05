class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        sys.setrecursionlimit(10 ** 6)

        def go(left, right):
            result = right - left + 1
            if left > right:
                return 0
            if left == right:
                return result
            if s[left] == s[right]:
                removal = s[left]
                while left <= right and s[left] == removal:
                    left += 1
                while right >= left and s[right] == removal:
                    right -= 1
                result = min(result, go(left, right))
            return result
        return go(0, n - 1)
