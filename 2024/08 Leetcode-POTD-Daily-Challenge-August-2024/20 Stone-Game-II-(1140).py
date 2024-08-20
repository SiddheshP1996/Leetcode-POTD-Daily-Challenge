class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        pilesLength = len(piles)
        cache = {}

        def execute(i, M, player):
            if i == pilesLength:
                return (0, 0)
            
            if (i, M, player) in cache:
                return cache[(i, M, player)]
            
            best = (0, 0)
            sumHere = 0
            
            for j in range(i, min(i + M, pilesLength)):
                newM = j - i + 1
                sumHere += piles[j]
                newBoundedM = min(max(2 * newM, M), pilesLength - j)
                alice, bob = execute(j + 1, newBoundedM, (player + 1) % 2)
                take = [alice, bob]
                take[player] += sumHere
                
                if take[player] >= best[player]:
                    best = (take[0], take[1])
                    
            cache[(i, M, player)] = best
            return best

        result = execute(0, 2, 0)[0]
        return result
