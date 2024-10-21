class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def execute(i, seen=set()):
            result = 0
            if i < len(s):
                for j in range(i + 1, len(s) + 1): 
                    if s[i:j] not in seen: 
                        seen.add(s[i:j])
                        result = max(result, 1 + execute(j, seen))
                        seen.remove(s[i:j])
            return result 
            
        return execute(0)
