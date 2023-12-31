class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 255
        for character in s:
            count[ord(character)] += 1
        for character in t:
            count[ord(character)] -= 1

        for k in count:
            if k != 0:
                return False

        return True
