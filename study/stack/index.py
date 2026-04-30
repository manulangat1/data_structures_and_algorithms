"""
Is a data structure that stores items in a Last In First out manner.
"""

import random


class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "<-->".join(values)

    def isEmpty(self):
        return len(self.list) == 0

    # isFull does not work.

    def push(self, value):
        return self.list.append(value)

    def peek(self):
        return self.list[len(self.list) - 1]

    def pop(self):
        if self.isEmpty():
            return
        return self.list.pop()


myStack = Stack()
print(myStack)
print(myStack)

for _ in range(10):
    myStack.push(random.randint(10, 1000))
print(myStack)
print(myStack.peek())
