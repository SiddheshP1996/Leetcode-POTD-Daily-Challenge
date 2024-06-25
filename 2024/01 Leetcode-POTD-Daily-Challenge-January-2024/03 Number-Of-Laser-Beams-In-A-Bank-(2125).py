class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n = len(bank)

        bankIntegerArray = []
        for i in range(n):
            row = sum([int(x) for x in bank[i]])
            if row == 0:
                continue
            bankIntegerArray.append(row)
        finalResult = 0
        m = len(bankIntegerArray)
        for i in range(1, m):
            result = (bankIntegerArray[i - 1] * bankIntegerArray[i])
            finalResult += result
        return finalResult
