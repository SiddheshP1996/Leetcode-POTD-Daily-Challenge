class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def ifPalindrome(character):
            leftWord = 0
            rightWord = len(character) - 1
            while leftWord <= rightWord:
                if character[leftWord] == character[rightWord]:
                    leftWord += 1
                    rightWord -= 1
                else:
                    return False
            return True

        for word in words:
            if ifPalindrome(word):
                return word
        return ""
