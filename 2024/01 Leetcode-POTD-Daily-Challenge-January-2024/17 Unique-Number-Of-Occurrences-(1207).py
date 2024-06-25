class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        numberSeenInArray = set()
        for v in count.values():
            if v in numberSeenInArray:
                return False
            numberSeenInArray.add(v)
        return True