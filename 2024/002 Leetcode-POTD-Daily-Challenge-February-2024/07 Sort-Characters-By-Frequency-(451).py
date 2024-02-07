from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        frequencyList = list(s)
        result = [n for n, count in Counter(frequencyList).most_common() for i in range(count)]
        return "".join(result)
