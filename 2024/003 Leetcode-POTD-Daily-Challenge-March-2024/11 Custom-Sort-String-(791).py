class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = collections.Counter(s)
        result = []

        for char in order:
            result.append(char * counter.pop(char, 0))
            
        for char, count in counter.items():
            result.append(char * count)
        return ''.join(result)
