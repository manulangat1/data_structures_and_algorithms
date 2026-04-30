import random

"""

space and time complexity is 0(1)
"""


class Node:
    def __init__(self, value=None, next=None):
        self.val = value
        self.next = next

    def __repr__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.head = None


class Stack:
    def __init__(self):
        self.linkedList = LinkedList()

    def isEmpty(self):
        return self.linkedList.head is None

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.linkedList.head
        self.linkedList.head = newNode

    def traverse(self):
        node = self.linkedList.head

        while node and node.next:
            yield node.val
            node = node.next

    def pop(self):
        self.linkedList.head = self.linkedList.head.next
        # return self.linkedList.head
        return self.linkedList

    def peek(self):
        return self.linkedList.head


myStack = Stack()
print(myStack.isEmpty())
for _ in range(10):
    myStack.push(random.randint(10, 1000))
print(myStack.isEmpty())
print([str(x) for x in myStack.traverse()])
print(myStack.peek())
