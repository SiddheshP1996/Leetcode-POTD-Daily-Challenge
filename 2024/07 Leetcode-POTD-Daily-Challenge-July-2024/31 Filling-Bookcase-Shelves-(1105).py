from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        numberOfBooks = len(books)
        dp = [0] * (numberOfBooks + 1)
        for i in range(1, numberOfBooks + 1):
            width, height = books[i - 1]
            dp[i] = dp[i - 1] + height
            j = i - 1
            while j > 0 and width + books[j - 1][0] <= shelfWidth:
                width += books[j - 1][0]
                height = max(height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + height)
                j -= 1
        return dp[numberOfBooks]
