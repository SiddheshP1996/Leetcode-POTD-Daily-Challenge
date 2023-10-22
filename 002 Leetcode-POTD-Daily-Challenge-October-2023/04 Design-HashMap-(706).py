class MyHashMap:

    def __init__(self):
        self._size = 1000
        self._data =[[] for _ in range(self._size)]

    def hash(self, key):
        return key % self._size

    def put(self, key: int, value: int) -> None:
        self._data[self.hash(key)].append((key, value))

    def get(self, key: int) -> int:
        for (k, v) in reversed(self._data[self.hash(key)]):
            if k == key: return v
        return -1

    def remove(self, key: int) -> None:
        self.put(key, -1)

    # Your MyHashMap object will be instantiated and called as such:
    # obj = MyHashMap()
    # obj.put(key,value)
    # param_2 = obj.get(key)
    # obj.remove(key)
