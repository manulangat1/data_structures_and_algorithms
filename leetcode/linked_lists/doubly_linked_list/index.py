"""
- Each node except the head and tail have ref to the next and prev nodes.
"""

import random


class ListNode:
    def __init__(self, value=None, next=None, prev=None):
        self.val = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        """
        time complexity is O(n)
        space complexity is 0(1)
        """
        head = self.head
        while head:
            yield head.val
            head = head.next

    def printL(self):
        """
        time complexity is O(n)
        space complexity is 0(1)
        """
        head = self.head
        count = 0
        while head:
            print(
                # "*" * count,
                head.val
            )
            count += 1
            head = head.next

        return

    def search(self, value):
        head = self.head
        while head:
            if head.val == value:
                return True
            head = head.next
        return False

    def insertion(self, val, posn):
        newNode = ListNode(val)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            if posn == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif posn == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

            else:
                count, tempNode = 0, self.head
                while count < posn - 1 and tempNode.next:
                    tempNode = tempNode.next
                    count += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                if newNode.next:
                    newNode.next.prev = newNode
                else:
                    self.tail = newNode
                tempNode.next = newNode

    def reverseTraversal(self):
        tempNode = self.tail
        while tempNode:
            print(tempNode.val)
            tempNode = tempNode.prev

    def deletion(self, posn):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            if posn == 0:
                self.head = self.head.next
                self.head.prev = None
            elif posn == -1:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                currNode, count = self.head, 0

                while count < posn - 1 and currNode.next:
                    currNode = currNode.next
                    count += 1
                currNode.next = currNode.next.next
                currNode.next.prev = currNode

    def deleteEntireDLL(self):
        self.head = None
        # self.head.next = None
        # self.tail.prev = None
        self.tail = None


myDLL = DoublyLinkedList()
print([i for i in myDLL])
myDLL.printL()

print(myDLL.search(1))

for k in range(5):
    myDLL.insertion(random.randint(0, 100), k)
# myDLL.printL()
print(random.randint(0, 100))
myDLL.insertion(random.randint(0, 100), 0)
myDLL.insertion(random.randint(0, 100), 0)
myDLL.insertion(random.randint(0, 100), 0)
myDLL.insertion(random.randint(0, 100), 4)
print([i for i in myDLL])


myDLL.reverseTraversal()

myDLL.deleteEntireDLL()
print("After deleting entire DLL")
print([i for i in myDLL])
