class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        leftPile = 0
        rightPile = n - 1
        results = 0
        while leftPile <= rightPile:
            aliceHasCoins = piles[rightPile]
            rightPile -= 1
            tempPileStore = piles[rightPile]
            rightPile -= 1
            bobHasCoins = piles[leftPile]
            leftPile += 1
            results += tempPileStore
        return results
