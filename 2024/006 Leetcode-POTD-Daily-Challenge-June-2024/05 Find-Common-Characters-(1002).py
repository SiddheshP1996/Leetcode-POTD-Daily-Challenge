class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        count = [[0 for _ in range(26)] for _ in range(n)]
        result = []
        for i in range(n):
            for character in words[i]:
                count[i][ord(character) - ord('a')] += 1
        for i in range(26):
            common = count[0][i]
            for j in range(n):
                common = min(common, count[j][i])
            for _ in range(common):
                result.append(chr(i + ord('a')))
        return result
