class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        countOfFive = 0
        countOfTen = 0
        for b in bills:
            if b == 5: 
                countOfFive += 1
            elif b == 10:
                if countOfFive == 0:
                    return False
                countOfTen += 1
                countOfFive -= 1
            else:
                if (countOfFive >= 1 and countOfTen >=1 ):
                    countOfFive -= 1 
                    countOfTen -= 1
                elif countOfFive >= 3:
                    countOfFive -= 3 
                else:
                    return False
        return True
