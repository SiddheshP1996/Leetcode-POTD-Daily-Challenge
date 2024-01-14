class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        counter1 = [0] * 26
        counter2 = [0] * 26

        n = len(word1)
        
        for i in range(n):
            counter1[ord(word1[i]) - ord('a')] += 1
            counter2[ord(word2[i]) - ord('a')] += 1
            
        for i in range(26):
            if (counter1[i] == 0 and counter2[i] > 0) or (counter2[i] == 0 and counter1[i] > 0):
                return False

        counter1.sort()
        counter2.sort()
        for i in range(26):
            if counter1[i] != counter2[i]:
                return False
        return True
