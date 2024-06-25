class RandomizedSet:

    def __init__(self):
        self.numbers = {}
        self.numbersArray = []

    def insert(self, val: int) -> bool:
        if val in self.numbers:
            return False
        self.numbers[val] = len(self.numbers)
        self.numbersArray.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.numbers:

            numberIndex = self.numbers[val]
            lastNumber = self.numbersArray[-1]
            self.numbersArray[numberIndex] = self.numbersArray[-1]
            self.numbersArray[-1] = val
            self.numbers.pop(val)
            self.numbersArray.pop()
            if lastNumber != val:
                self.numbers[lastNumber] = numberIndex
            return True
        return False

    def getRandom(self) -> int:
        return self.numbersArray[random.randint(0,len(self.numbersArray) - 1)]

"""
Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(val)
param_2 = obj.remove(val)
param_3 = obj.getRandom()
"""