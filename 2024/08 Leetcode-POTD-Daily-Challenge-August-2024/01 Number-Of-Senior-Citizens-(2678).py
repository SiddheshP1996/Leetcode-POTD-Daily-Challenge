class Solution:
    def countSeniors(self, details: List[str]) -> int:
        countOfSeniors = 0
        for personel in details:
            age = int(personel[11] + personel[12])
            if age > 60:
                countOfSeniors += 1
        return countOfSeniors
