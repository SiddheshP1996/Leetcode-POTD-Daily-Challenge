from heapq import heappop, heappush

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()
        i = 0
        highestCapital = []
        
        while k > 0:
            while i < n and projects[i][0] <= w:
                heappush(highestCapital, -projects[i][1])
                i += 1
            if not highestCapital:
                break
            w -= heappop(highestCapital)
            k -= 1
            
        return w
