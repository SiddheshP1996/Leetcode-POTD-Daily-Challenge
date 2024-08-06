from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        letters = Counter(word)
        lettersSorted = sorted([(-count, l) for (l, count) in letters.items()])
        lettersMap = {
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
        }
        cost = [0] * 26
        letterKeys = list(lettersMap.keys())
        letterIndex = 0

        for _, l in lettersSorted:
            lettersMap[letterKeys[letterIndex]].append(l)
            cost[ord(l) - ord('a')] = len(lettersMap[letterKeys[letterIndex]])
            letterIndex += 1
            letterIndex %= (len(letterKeys))

        totalWordCost = 0
        for c in word:
            totalWordCost += cost[ord(c) - ord('a')]
        return totalWordCost
