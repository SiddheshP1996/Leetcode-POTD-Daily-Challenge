class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        arr = [0] * n

        for a, b in roads:
            arr[a] += 1
            arr[b] += 1

        return sum(map(mul, sorted(arr), range(1, 1 + n)))
