class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = ' ' + sentence
        searchWord = ' ' + searchWord
        n, m = len(sentence), sentence.find(searchWord)
        if m == -1: return -1
        return 1+sentence[:m].count(' ')
