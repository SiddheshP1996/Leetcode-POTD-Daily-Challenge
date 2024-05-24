class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        wordsCounter = [[0 for _ in range(26)] for _ in range(n)]
        for i in range(n):
            for character in words[i]:
                wordsCounter[i][ord(character) - ord('a')] += 1

        wordScore = [0] * n
        for i in range(n):
            scores = 0
            for j in range(26):
                scores += score[j] * wordsCounter[i][j]
            wordScore[i] = scores

        def fetchWordsAllowed(lettersCounter):
            allowed = 0
            for i in range(n):
                isAllowed = True
                for j in range(26):
                    if lettersCounter[j] < wordsCounter[i][j]:
                        isAllowed = False
                        break
                if isAllowed:
                    allowed |= (1 << i)
            return allowed

        def subtract(a, b):
            result = list(b)
            for i in range(26):
                result[i] -= a[i]
            return result

        cache = {}

        def execute(availableLetters, usedWords):
            scoreWords = 0
            if usedWords in cache:
                return cache[usedWords]
            allowedWords = fetchWordsAllowed(availableLetters)
            if allowedWords == 0:
                return scoreWords
            if usedWords == (1 << n) - 1:
                return scoreWords
            for i in range(n):
                if allowedWords & (1 << i) != 0 and usedWords & (1 << i) == 0:
                    remainingWords = subtract(wordsCounter[i], availableLetters)
                    scoreWords = max(scoreWords, wordScore[i] + execute(remainingWords, (1 << i) | usedWords))
            cache[usedWords] = scoreWords
            return scoreWords

        availableLettersCounter = [0] * 26
        for character in letters:
            availableLettersCounter[ord(character) - ord('a')] += 1

        return execute(availableLettersCounter, 0)
