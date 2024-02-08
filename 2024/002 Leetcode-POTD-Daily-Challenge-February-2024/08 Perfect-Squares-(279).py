squares = []
for i in range(1, 10001):
    square = math.sqrt(i)

    if square == int(square):
        squares.append(i)
has_cache = [False] * 10001
cache = [0] * 10001

class Solution:
    def numSquares(self, n: int) -> int:
        global squares
        global has_cache
        global cache
        INF = 10 ** 20
        def execute_squares(number):
            if number == 0:
                return 0
            if number < 0:
                return INF
            if has_cache[number]:
                return cache[number]
            result = INF
            for i in range(len(squares) - 1, -1, -1):
                result = min(result, 1 + execute_squares(number - squares[i]))
            has_cache[number] = True
            cache[number] = result
            return result
        return execute_squares(n)
