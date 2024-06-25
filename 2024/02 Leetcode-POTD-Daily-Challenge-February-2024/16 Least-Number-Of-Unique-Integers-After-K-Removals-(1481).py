class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = collections.Counter(arr)
        heap = [] 
        for uniqueValue, occurenceCount in count.most_common():
            heapq.heappush(heap,(occurenceCount, uniqueValue))
        
        for item in range(k):
            occurenceCount, uniqueValue = heapq.heappop(heap)
            occurenceCount -= 1
            if occurenceCount == 0:
                continue
            heapq.heappush(heap, (occurenceCount, uniqueValue))
        return len(heap)
