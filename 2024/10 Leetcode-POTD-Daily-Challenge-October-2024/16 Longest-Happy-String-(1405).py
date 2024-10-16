from heapq import heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = ""
        maxHeap = []
        for count, character in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heappush(maxHeap, (count, character))
                
        while maxHeap:
            count, character = heappop(maxHeap)
            if len(result) > 1 and result[-1] == result[-2] == character:
                if not maxHeap:
                    break
                count2, char2 = heappop(maxHeap)
                result += char2
                count2 += 1
                
                if count2:
                    heappush(maxHeap, (count2, char2))
            else:
                result += character
                count += 1
                
            if count:
                heappush(maxHeap, (count, character))
        return result
