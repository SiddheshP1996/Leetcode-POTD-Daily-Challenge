class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        prefixes = [0]

        for item in arr:
            prefixes.append(prefixes[-1] ^ item)

        for left, right in queries:
            result.append(prefixes[right + 1] ^ prefixes[left])
            
        return result
