# from leetcode.linked_lists.quiz.LinkedList import LinkedList

import random


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Queue:
    def __init__(self):
        self.ll = LinkedList()

    def __str__(self):
        return "->".join([str(x) for x in self.ll])

    def enqueue(self, nodeValue):
        newNode = Node(nodeValue)
        if self.ll.head is None:
            self.ll.head = newNode
            self.ll.tail = newNode
        else:
            self.ll.tail.next = newNode
            self.ll.tail = newNode

    def isEmpty(self):
        return self.ll.head is None

    def peek(self):
        node = self.ll.head
        return node

    def dequeu(self):
        node = self.ll.head
        self.ll.head = self.ll.head.next
        return node


myQ = Queue()
print(myQ)
for _ in range(10):
    num = random.randint(1, 999)

    myQ.enqueue(num)
    print(num)
    print()

print(myQ)

print(myQ.peek())

print(myQ.dequeu())
print(myQ)
