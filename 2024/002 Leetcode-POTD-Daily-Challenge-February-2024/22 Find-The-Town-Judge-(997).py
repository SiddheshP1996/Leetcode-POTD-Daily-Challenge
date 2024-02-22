class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0] * (n + 1)
        count_1 = [0] * (n + 1)
        for item_1, item_2 in trust:
            count[item_2] += 1
            count_1[item_1] += 1
        for element in range(1, n + 1 ):
            if count[element] == n - 1 and count_1[element] == 0 :
                return element
        return -1
