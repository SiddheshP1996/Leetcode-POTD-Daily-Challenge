class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        win = 0
        prev = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > prev:
                prev = arr[i]
                win = 0
            win += 1
            if win == k:
                break
        return prev
    