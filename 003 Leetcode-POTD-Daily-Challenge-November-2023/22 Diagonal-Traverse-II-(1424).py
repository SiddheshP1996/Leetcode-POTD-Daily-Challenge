import collections


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        diagonals = collections.defaultdict(list)
        results = []
        for i in range(n):
            for j in range(len(nums[i])):
                diagonals[(i + j)].append((i, j))
        for k, l in diagonals.items():
            i, j = l[0]
            u, v = l[-1]
            for f in range(len(l) - 1, -1, -1):
                (i, j) = l[f]
                results.append(nums[i][j])
        return results
