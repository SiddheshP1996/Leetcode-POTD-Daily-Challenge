class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.incrementStack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.incrementStack.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        index = len(self.stack) - 1
        result = self.stack[index] + self.incrementStack[index]
        if index > 0:
            self.incrementStack[index - 1] += self.incrementStack[index]
        self.stack.pop()
        self.incrementStack.pop()
        return result

    def increment(self, k: int, val: int) -> None:
        limit = min(k, len(self.stack)) - 1
        if limit >= 0:
            self.incrementStack[limit] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
