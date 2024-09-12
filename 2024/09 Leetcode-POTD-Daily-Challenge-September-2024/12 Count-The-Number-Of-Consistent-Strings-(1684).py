class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedString = set(allowed)
        count = 0

        for word in words:
            for character in word:
                if character not in allowedString:
                    count += 1
                    break
        return len(words) - count
