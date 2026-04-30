import random


class CircularQ:
    def __init__(self, maxSize):
        self.items = [None] * maxSize
        self.maxSize = maxSize
        self.top = -1
        self.start = -1

    def __str__(self):
        return "->".join([str(x) for x in self.items])

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        return self.top == -1

    def enqueue(self, value):
        if self.top + 1 == self.maxSize:
            self.top = 0
        else:
            self.top += 1
            if self.start == -1:
                self.start = 0
        self.items[self.top] = value
        return self.items


myCQ = CircularQ(10)

for _ in range(10):
    myCQ.enqueue(random.randint(1, 999))

print(myCQ)
