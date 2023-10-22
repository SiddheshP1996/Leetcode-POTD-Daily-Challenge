class Solution:
    def candy(self, ratings: List[int]) -> int:
        lengthR = len(ratings)
        result = [1] * lengthR

        for i in range(lengthR - 1):
            if ratings[i] < ratings[i + 1] and result[i + 1] <= result[i]:
                result[i + 1] = result[i] + 1
        ratings = ratings[::-1]
        result = result[::-1]

        for i in range(lengthR - 1):
            if ratings[i] < ratings[i + 1] and result[i + 1] <= result[i]:
                result[i + 1] = result[i] + 1
        return (sum(result))