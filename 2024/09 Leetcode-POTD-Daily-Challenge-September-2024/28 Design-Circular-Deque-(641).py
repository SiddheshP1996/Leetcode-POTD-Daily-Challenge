class MyCircularDeque:

    def __init__(self, k: int):
        self.initializeDeque = [-1] * k
        self.front = 0
        self.back = 0
        self.currentSize = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity

        self.initializeDeque[self.front] = value
        self.currentSize += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.initializeDeque[self.back] = value
        self.back = (self.back + 1) % self.capacity

        self.currentSize += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.initializeDeque[self.front] = -1
        self.front = (self.front + 1) % self.capacity

        self.currentSize -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        if self.back == 0:
            self.back = self.capacity - 1
        else:
            self.back -= 1

        self.initializeDeque[self.back] = -1
        self.currentSize -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.initializeDeque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        if self.back == 0:
            return self.initializeDeque[self.capacity - 1]
        else:
            return self.initializeDeque[self.back - 1]

    def isEmpty(self) -> bool:
        return self.currentSize == 0

    def isFull(self) -> bool:
        return self.currentSize == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
