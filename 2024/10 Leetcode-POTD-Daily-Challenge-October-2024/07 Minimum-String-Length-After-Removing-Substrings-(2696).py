class Solution:
    def minLength(self, s: str) -> int:
        characterStack = []
        for character in s:
            if not characterStack:
                characterStack.append(character)
                continue
            if character == "B" and characterStack[-1] == "A":
                characterStack.pop()
            elif character == "D" and characterStack[-1] == "C":
                characterStack.pop()
            else:
                characterStack.append(character)
        return len(characterStack)
