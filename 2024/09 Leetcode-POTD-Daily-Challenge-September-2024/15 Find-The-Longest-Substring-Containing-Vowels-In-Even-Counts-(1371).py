class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dictionary = defaultdict(int)
        vowels = {"a": 0, "e": 1, "i" : 2, "o" : 3, "u" : 4}
        count, result, dictionary[0] = 0, 0, -1

        for vowel, character in enumerate(s):
            if character in "aeiou":
                count ^= (1 << vowels[character])

            if count in dictionary:
                result = max(result, vowel - dictionary[count])
            else:
                dictionary[count] = vowel
        
        return result