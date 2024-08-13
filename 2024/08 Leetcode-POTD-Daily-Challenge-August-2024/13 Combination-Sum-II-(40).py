class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        n = len(candidates)
        candidates.sort()
        nextIndex = [n] * n 
        for i in range(n):
            for j in range(i + 1, n):
                if candidates[j] != candidates[i]:
                    nextIndex[i] = j
                    break

        def execute(i, targetHere, usedCandidates):
            if targetHere == 0:
                return result.append(list(usedCandidates))
            if targetHere < 0:
                return []
            if i == n:
                return []
            usedCandidates.append(candidates[i])
            execute(i + 1, targetHere - candidates[i], usedCandidates)
            usedCandidates.pop()
            execute(nextIndex[i], targetHere, usedCandidates)

        execute(0, target, [])
        return result
