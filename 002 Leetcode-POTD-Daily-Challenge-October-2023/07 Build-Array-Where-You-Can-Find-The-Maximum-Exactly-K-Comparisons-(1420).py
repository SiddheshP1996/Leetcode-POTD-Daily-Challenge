class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp = {}

        def rec(i, maxSoFar, remCost):
            # base case
            # if we got elements == n
            if i == n:
                """
                if we can find no more max elements which have all the elements lower than them on their left ( 
                this is what the algo mentioned in desc does)
                """
                if remCost == 0:
                    # we have found a way to form an array with given cond
                    return 1
                return 0
            if (i, maxSoFar, remCost) in dp:
                return dp[(i, maxSoFar, remCost)]
            # there are 2 possibilities to fill the ith position
            # 1. we do not choose a new maxSoFar , ie we choose an element
            # in the range 1 , maxSoFar (so possibilities = maxSoFar)

            # since we have not taken a new maxSoFar , the maxSOFar and remCost argument remain same
            ans = (maxSoFar * rec(i + 1, maxSoFar, remCost)) % MOD

            # 2. we take a new maxSoFar , then we have a range of maxSoFar+1,m(inclusive)
            for newMaxSoFar in range(maxSoFar + 1, m + 1):
                ans = (ans + rec(i + 1, newMaxSoFar, remCost - 1)) % MOD
            dp[(i, maxSoFar, remCost)] = ans
            return dp[(i, maxSoFar, remCost)]

        MOD = 10 ** 9 + 7
        return rec(0, 0, k)
