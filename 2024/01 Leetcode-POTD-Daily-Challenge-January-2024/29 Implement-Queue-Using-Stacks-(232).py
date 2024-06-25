class MyQueue:

    def __init__(self):
        self._items = []

    def push(self, x: int) -> None:
        self._items.insert(0, x)

    def pop(self) -> int:
        return self._items.pop()

    def peek(self) -> int:
        return self._items[-1]

    def empty(self) -> bool:
        return not self._items

"""
Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
"""
