class Solution:
    def strangePrinter(self, s: str) -> int:
        INF = 10 ** 20
        n = len(s)
        
        @cache
        def execute(left, right):
            if left == right:
                return 1
            
            if left > right:
                return 0
            
            result = execute(left, left) + execute(left + 1, right)
            
            for i in range(left + 1, right + 1):
                if  s[left] == s[i]:
                    result = min(result, execute(left, i - 1) + execute(i + 1, right))
            return result

        return execute(0, n - 1)
