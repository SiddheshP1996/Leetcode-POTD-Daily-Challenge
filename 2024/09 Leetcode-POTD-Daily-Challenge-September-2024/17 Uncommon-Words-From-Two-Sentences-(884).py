class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        allString = s1.split(' ')
        allString += s2.split(' ')
        counter = Counter(allString)

        result = []
        for string, count in counter.items():
            if count == 1:
                result.append(string)
        return result
