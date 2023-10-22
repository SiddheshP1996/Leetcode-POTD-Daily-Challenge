class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        countOfA = 0
        countOfB = 0
        lengthOfString = len(colors)
        for i in range(lengthOfString - 2):
            if colors[i: i + 3] == 'AAA':
                countOfA += 1
            elif colors[i: i + 3] == 'BBB':
                countOfB += 1
        return countOfA > countOfB
