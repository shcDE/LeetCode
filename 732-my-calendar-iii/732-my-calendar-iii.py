class MyCalendarThree:

    def __init__(self):
        self.events = []

    def calculator(self, x):
        k = out = 0
        for e in x:
            k = k+1 if e[1] == 'S' else k-1
            out = max(k, out)
        return out
        
    def book(self, start: int, end: int) -> int:
        bisect.insort(self.events,(start,'S'))
        bisect.insort(self.events,(end,'E'))
        return self.calculator(self.events)

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)