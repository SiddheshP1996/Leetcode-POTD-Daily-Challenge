class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        totalBuy = 0

        for i, x in enumerate(tickets):
            if i <= k:
                totalBuy += min(tickets[i], tickets[k])
            else:
                totalBuy += min(tickets[i], tickets[k] - 1)

        return totalBuy
