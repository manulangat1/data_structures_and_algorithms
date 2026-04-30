import random


class Node:
    def __init__(self, value, next=None, prev=None):
        self.val = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class LinkedList:
    def __int__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

    def __str__(self):
        values = [str(x.val) for x in self]
        return " -> ".join(values)

    def __len__(self):
        count = 0
        currNode = self.head
        while currNode:
            count += 1
            currNode = currNode.next
        return count

    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None

        for i in range(n):
            self.add(random.randint(min_value, max_value))
        return self


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
