class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for array in sorted(arr):
            rank.setdefault(array, len(rank) + 1)
        return map(rank.get, arr)
