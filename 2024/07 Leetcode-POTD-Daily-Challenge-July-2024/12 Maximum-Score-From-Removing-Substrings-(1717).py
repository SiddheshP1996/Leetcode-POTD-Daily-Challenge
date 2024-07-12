class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        totalScore = 0
        highPriorityPair = "ab" if x > y else "ba"
        lowPriorityPair = "ba" if highPriorityPair == "ab" else "ab"

        stringAfterFirstPass = self.removeSubstring(s, highPriorityPair)
        removedPairsCount = (len(s) - len(stringAfterFirstPass)) // 2

        totalScore += removedPairsCount * max(x, y)

        stringAfterSecondPass = self.removeSubstring (
            stringAfterFirstPass, lowPriorityPair
        )
        removedPairsCount = (
            len(stringAfterFirstPass) - len(stringAfterSecondPass)
        ) // 2

        totalScore += removedPairsCount * min(x, y)

        return totalScore

    def removeSubstring(self, input: str, targetPair: str) -> str:
        characterStack = []

        for currentCharacter in input:
            if (
                currentCharacter == targetPair[1]
                and characterStack
                and characterStack[-1] == targetPair[0]
            ):
                characterStack.pop()
            else:
                characterStack.append(currentCharacter)

        return "".join(characterStack)
