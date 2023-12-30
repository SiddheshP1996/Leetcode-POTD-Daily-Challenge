class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)

        count = collections.Counter()
        for word in words:
            for character in word:
                count[character] += 1

        for value in count.values():
            if value % n != 0:
                return False
        return True
