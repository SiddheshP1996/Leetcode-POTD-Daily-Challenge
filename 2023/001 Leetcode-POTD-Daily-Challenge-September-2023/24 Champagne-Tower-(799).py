class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glassTower = [poured]
        for row in range(query_row):
            next_row = [0.0] * (row + 2)
            for glass in range(len(glassTower)):
                flow = (glassTower[glass] - 1.0) / 2.0
                if flow > 0.0:
                    next_row[glass] += flow
                    next_row[glass + 1] += flow
            glassTower = next_row
        return min(1.0, glassTower[query_glass])
