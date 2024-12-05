class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start += '@'
        target += '@'
        i, j = 0, 0
        while i < len(start) or j < len(start):
            while i < len(start) and start[i] == '_': i += 1
            while j < len(start) and target[j] == '_': j += 1
            c = start[i]
            if c != target[j]: return False
            if c == 'L' and i < j: return False
            if c == 'R' and i > j: return False
            i += 1
            j += 1
        return True
