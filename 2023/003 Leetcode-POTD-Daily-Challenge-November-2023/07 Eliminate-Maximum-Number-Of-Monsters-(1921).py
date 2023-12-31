from math import ceil


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        noOfMonsters = []
        for i in range(len(dist)):
            noOfMonsters.append(ceil(dist[i] / speed[i]))
        noOfMonsters.sort()
        count = 1
        for i in range(1, len(noOfMonsters)):
            if noOfMonsters[i] >= (i + 1):
                count += 1
            else:
                break
        print(count)
        return max(count, 1)
