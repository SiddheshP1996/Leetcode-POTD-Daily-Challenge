class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        results = 0
        for wordInWords in words:
            flag = 1
            for char in wordInWords:
                if chars.count(char) < wordInWords.count(char):
                    flag = 0
                    break
            if flag:
                results += len(wordInWords)
        return results
