from collections import deque
from heapq import heapify, heappop

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        result = [None] * n
        heapq.heapify(deck)
        stack = collections.deque( [i for i in range(n)])
        def cardShuffle(shouldStack):
            if len(deck) == 0:
                return
            nextIndex = stack.popleft()
            if shouldStack:
                stack.append(nextIndex)
            else:
                result[nextIndex] = heapq.heappop(deck)
            return cardShuffle(not shouldStack)
        cardShuffle(False)
        return result
