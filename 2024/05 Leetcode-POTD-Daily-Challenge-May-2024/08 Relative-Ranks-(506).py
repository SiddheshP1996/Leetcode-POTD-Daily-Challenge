class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        ranks = sorted([(-score[i], i) for i in range(n)])
        medalNames = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result = [""] * n
        for i in range(n):
            _, position = ranks[i]
            if i < len(medalNames):
                result[position] = medalNames[i]
            else:
                result[position] = str(i + 1)

        return result
