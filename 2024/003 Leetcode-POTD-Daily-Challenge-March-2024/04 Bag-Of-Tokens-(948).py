class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        INF = 10 ** 20
        tokens.sort()
        leftToken = 0
        rightToken = n - 1

        resultToken = 0
        while leftToken <= rightToken:
            if tokens[leftToken] <= power:
                resultToken += 1
                power -= tokens[leftToken]
                leftToken += 1
            elif resultToken >= 1 and rightToken - leftToken > 1:
                power += tokens[rightToken]
                resultToken -= 1
                rightToken -= 1
            else:
                break
        return resultToken
