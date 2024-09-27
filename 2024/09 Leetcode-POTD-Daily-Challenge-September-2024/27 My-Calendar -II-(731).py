class MyCalendarTwo:
    def __init__(self):
        self.singleEvent = []
        self.doubleEvent = []

    def book(self, start: int, end: int) -> bool:
        for begin, close in self.doubleEvent:
            if max(start, begin) < min(end, close):
                return False
        
        for begin, close in self.singleEvent:
            if max(start, begin) < min(end, close):
                self.doubleEvent.append((max(start, begin), min(end, close)))
        
        self.singleEvent.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start, end)
