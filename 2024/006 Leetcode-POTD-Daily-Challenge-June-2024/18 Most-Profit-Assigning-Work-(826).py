class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        combo = list(zip(difficulty, profit))
        combo.sort()
        n = len(combo)
        maximumDifficulty = combo[-1][0]
        maximumProfit = [0] * (maximumDifficulty + 1)
        j = 0
        for i in range(1, (maximumDifficulty + 1)):
            profitMax = maximumProfit[i - 1]
            while j < n and combo[j][0] == i:
                profitMax = max(combo[j][1], profitMax)
                j += 1
            maximumProfit[i] = profitMax
        result = 0
        for work in worker:
            result += maximumProfit[min(work, maximumDifficulty)]
        return result
