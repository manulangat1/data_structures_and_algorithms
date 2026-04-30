class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


# class Q:
#     def __init__(self):
#         self.items = []


class Stack:
    def __init__(self):
        self.top = None
        self.minNode = None

    def min(self):
        return self.minNode.value

    def push(self, item):
        if self.minNode and self.minNode.value < item:
            self.minNode = Node(self.minNode.value, self.minNode)
        else:
            self.minNode = Node(item, self.minNode)
        self.top = Node(item, self.top)

    def pop(self):
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next
        return item
