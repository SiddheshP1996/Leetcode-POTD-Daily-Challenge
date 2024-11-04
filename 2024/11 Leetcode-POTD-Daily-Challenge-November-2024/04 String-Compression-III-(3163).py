class Solution:
    def compressedString(self, word: str) -> str:
        stringCompress = ""
        count = 1
        character = word[0]
        for i in range(1, len(word)):
            if word[i] == character and count < 9:
                count += 1
            else:
                stringCompress += str(count) + character
                character = word[i]
                count = 1
        stringCompress += str(count) + character
        return stringCompress
