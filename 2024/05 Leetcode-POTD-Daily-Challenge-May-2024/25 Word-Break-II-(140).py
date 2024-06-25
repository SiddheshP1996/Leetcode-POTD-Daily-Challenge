class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memoryDictionary = {}
        def wordsEndingIn(i):
            if i == len(s):
                return [""]
            if i in memoryDictionary:
                return memoryDictionary[i]
            resultArray = []
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict:
                    for tail in wordsEndingIn(j):
                        if tail != '':
                            resultArray.append(s[i:j] + " " + tail) 
                        else:
                            resultArray.append(s[i:j])
            memoryDictionary[i] = resultArray
            return resultArray
        return wordsEndingIn(0)
