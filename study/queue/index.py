"""
* DS that stores items in a FIFO manner.
* There are 2 impl patterns using a list. Queue without capacity and a circular queue.
"""

import random


class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return "->".join([str(x) for x in self.items])

    def isEmpty(self):
        return len(self.items) > 0

    def enqueue(self, value):
        return self.items.append(value)

    def peek(self):
        return self.items[0]

    def dequeue(self):
        return self.items.pop(0)


myQ = Queue()
for _ in range(10):
    myQ.enqueue(random.randint(1, 999))

print(myQ)
