from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        isPalindrome = 0
        longest = 0
        for character in set(s):
            if count[character] % 2 == 0:
                longest += count[character]
            else:
                longest += (count[character] - 1)
                isPalindrome = 1
        longest += isPalindrome
        return longest
