class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result = []
        i = 0
        n = len(word)
        while i < n:
            result.append(word[i])
            if word[i] == ch:
                result.reverse()
                break
            i += 1
        i += 1
        while i < n:
            result.append(word[i])
            i += 1
        return "".join(result)
