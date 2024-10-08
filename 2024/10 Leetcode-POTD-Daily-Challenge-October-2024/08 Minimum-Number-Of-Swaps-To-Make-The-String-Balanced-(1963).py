class Solution:
    def minSwaps(self, s: str) -> int:
        openBracket = 0
        for character in s:
            if openBracket > 0 and character == ']':
                openBracket -= 1
            elif character == '[':
                openBracket += 1
        return (openBracket + 1) // 2
