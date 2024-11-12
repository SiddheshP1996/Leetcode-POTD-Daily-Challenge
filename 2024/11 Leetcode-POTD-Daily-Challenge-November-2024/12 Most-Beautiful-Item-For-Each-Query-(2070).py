class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        maxItem = float('inf')
        result = [[0, 0, maxItem]]    
        items.sort(key=lambda x: x[0])

        for price, beauty in items:
            lastBracket = result[-1]
            if beauty > lastBracket[1]:
                result[-1][2] = price
                result.append([price, beauty, maxItem])

        finalResult = []
        for x in queries:
            for i in range(len(result) - 1, -1, -1):
                if result[i][0] <= x:
                    finalResult.append(result[i][1])
                    break

        return finalResult
