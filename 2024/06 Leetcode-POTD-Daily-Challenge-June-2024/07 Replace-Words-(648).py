from heapq import heappush

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = {'#': {}}

        def buildTrie(string):
            current = root['#']
            for character in string:
                if character in current:
                    current = current[character]
                else:
                    current[character] = {}
                    current = current[character]
            if '*' in current:
                heappush(current['*'], (len(string), string))
            else:
                current['*'] = [(len(string), string)]

        def getShortest(string):
            current = root['#']
            for character in string:
                if character in current:
                    current = current[character]
                else:
                    return string
                if '*' in current:
                    _, shorter = current['*'][0]
                    return shorter
            return string

        for word in dictionary:
            buildTrie(word)

        result = sentence.split(' ')
        n = len(result)

        for i in range(n):
            result[i] = getShortest(result[i])
        return " ".join(result)
