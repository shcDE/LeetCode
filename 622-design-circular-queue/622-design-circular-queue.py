class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [0 for i in range(k)]
        self.k = k
        self.front = 0
        self.back = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.data[self.back] = value
            self.back = (self.back+1)%self.k
            self.size += 1
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front + 1)%self.k
            self.size -= 1
            return True
        return False
        

    def Front(self) -> int:
        if not self.isEmpty():
            return self.data[self.front]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.data[self.back - 1]
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()