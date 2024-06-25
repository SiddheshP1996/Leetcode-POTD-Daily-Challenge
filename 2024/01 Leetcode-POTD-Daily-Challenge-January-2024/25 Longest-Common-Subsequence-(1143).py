class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        cache = [[0 for string_len in range(m)] for string_len in range(n)]
        has_cache = [[False for string_len in range(m)] for string_len in range(n)]
        def execute_subsequence(i, j):
            if i == n or j == m:
                return 0
            if has_cache[i][j]:
                return cache[i][j]
            result = 0
            if text1[i] == text2[j]:
                result = 1 + execute_subsequence(i + 1, j + 1)
            result = max(result, execute_subsequence(i, j + 1))
            result = max(result, execute_subsequence(i + 1, j))
            has_cache[i][j] = True
            cache[i][j] = result
            return result
            
        return execute_subsequence(0, 0)
