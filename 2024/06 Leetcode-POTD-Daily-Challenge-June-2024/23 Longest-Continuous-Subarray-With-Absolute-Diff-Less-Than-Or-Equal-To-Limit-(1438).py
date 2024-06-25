class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        logN = n.bit_length()
        maxs = [[0 for _ in range(logN)] for _ in range(n)]
        mins = [[0 for _ in range(logN)] for _ in range(n)]
        for i in range(n):
            maxs[i][0] = nums[i]
            mins[i][0] = nums[i]
        for j in range(1, logN):
            for i in range(n - (1 << j) + 1):
                maxs[i][j] = max(maxs[i][j - 1], maxs[i + (1 << (j - 1))][j - 1])
                mins[i][j] = min(mins[i][j - 1], mins[i + (1 << (j - 1))][j - 1])

        def getMinimum(left, right):
            logRange = (right - left + 1).bit_length() - 1
            start = right - (1 << logRange) + 1
            return min(mins[left][logRange], mins[start][logRange])

        def getMaximum(left, right):
            logRange = (right - left + 1).bit_length() - 1
            start = right - (1 << logRange) + 1
            return max(maxs[left][logRange], maxs[start][logRange])

        def good(size):
            for i in range(n - size + 1):
                minimumInRange = getMinimum(i, i + size - 1)
                maximumInRange = getMaximum(i, i + size - 1)
                if abs(maximumInRange - minimumInRange) <= limit:
                    return True
            return False

        left = 0
        right = n + 1
        result = 0
        while left < right:
            middle = (left + right) // 2
            if good(middle):
                result = middle
                left = middle + 1
            else:
                right = middle
        return result
