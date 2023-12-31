class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets <= 1:
            return 0
        if buckets == 2:
            return 1
        maximumTurns = minutesToTest // minutesToDie

        pigs = 0
        dimensionSearch = (maximumTurns + 1) ** pigs
        while dimensionSearch < buckets:
            pigs += 1
            dimensionSearch = (maximumTurns + 1) ** pigs
        return pigs
