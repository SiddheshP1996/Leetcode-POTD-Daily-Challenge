class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        numbers = list(range(n))
        index = 0 
        while len(numbers) > 1: 
            index = (index + k - 1) % len(numbers)
            numbers.pop(index)
        return numbers[0] + 1
