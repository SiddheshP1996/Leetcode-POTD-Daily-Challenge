class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        leftItem = 0
        rightItem = 0
        result = 0
        n = len(s)
        totalCost = 0
        while rightItem < n:
            costPresent = abs(ord(s[rightItem]) - ord(t[rightItem]))
            totalCost += costPresent
            while totalCost > maxCost and leftItem <= rightItem:
                totalCost -= abs(ord(s[leftItem]) - ord(t[leftItem]))
                leftItem += 1
            result = max(result, (rightItem - leftItem + 1))
            rightItem += 1
        return result
