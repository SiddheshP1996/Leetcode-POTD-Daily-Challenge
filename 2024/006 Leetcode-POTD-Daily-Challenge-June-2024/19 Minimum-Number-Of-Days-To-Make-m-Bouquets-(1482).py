class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n: return -1

        def functionF(d):
            length, bouquet = 0, 0
            i = 0
            while i < n:
                while i < n and bloomDay[i] <= d:
                    length += 1
                    if length == k:
                        bouquet += 1
                        length = 0
                    i += 1
                if i < n and bloomDay[i] > d: length = 0
                if bouquet > m: return True
                i += 1
            return bouquet >= m

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            middle = left + (right - left) // 2
            if functionF(middle):
                right = middle
            else:
                left = middle + 1
        return left
