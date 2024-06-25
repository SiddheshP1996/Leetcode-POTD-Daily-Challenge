from heapq import heappush, heappop

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        qualityCounts = len(quality)
        minimumCost = float("inf")
        qualityTillNow = 0
        wageQualityRatio = []

        for i in range(qualityCounts):
            heappush(wageQualityRatio, (wage[i] / quality[i], quality[i]))

        highQualityWorkers = []

        for i in range(qualityCounts):
            ratio, currentQuality = heappop(wageQualityRatio)
            qualityTillNow += currentQuality
            heappush(highQualityWorkers, -currentQuality)

            if len(highQualityWorkers) > k:
                qualityTillNow += heappop(highQualityWorkers)

            if len(highQualityWorkers) == k:
                minimumCost = min(minimumCost, qualityTillNow * ratio)

        return minimumCost
