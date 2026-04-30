"""
Is a LL where each node has a ref to the next and prev node. The tail has a ref to the head and head has a ref to the tail.
"""


class ListNode:
    def __init__(self, value=None, next=None, prev=None):
        self.val = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class CircularDoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next

            if tempNode == self.head:
                break

    def traverse(self):
        tempNode = self.head
        count = 0
        while tempNode:
            print("*" * count, tempNode)
            tempNode = tempNode.next
            count += 1

            if tempNode == self.head:
                break

    def reverseTraversal(self):
        tempNode = self.tail
        while tempNode:
            print(tempNode)
            tempNode = tempNode.prev
            if tempNode == self.tail:
                break

    # creation of CDLL
    def createCDLL(self, nodeValue):
        newNode = ListNode(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode

    def insertion(self, nodeValue, posn):
        newNode = ListNode(nodeValue)
        if self.head is None:
            self.head, self.tail = newNode, newNode
            newNode.prev = newNode
            newNode.next = newNode

        else:
            if posn == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.head = newNode
            elif posn == -1:
                newNode.next = self.head
                self.head.prev = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                # loop till  you get the posn.
                tempNode = self.head
                count = 0
                while count < posn - 1:
                    tempNode = tempNode.next
                    count += 1
                    if tempNode == self.head:
                        print("Breaking up!")
                        break
                print(tempNode)
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
                # If inserting after tail, update tail
                if tempNode == self.tail:
                    self.tail = newNode

    def deletion(self, posn):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            if posn == 0:
                """
                1. change the tail next  to node after next.
                2. set the head to the node after next.
                3.
                """
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
            elif posn == -1:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
            else:
                tempNode = self.head
                count = 0
                while count < posn - 1:
                    tempNode = tempNode.next
                    count += 1
                    if tempNode == self.head:
                        print("Breaking up!")
                        break
                nodeToDelete = tempNode.next

                tempNode.next = nodeToDelete.next
                nodeToDelete.next.prev = tempNode

                # update tail if needed
                if nodeToDelete == self.tail:
                    self.tail = tempNode

    def deleteEntireCDLL(self):
        if self.head is None:
            return

        self.tail.next = None
        self.head.prev = None

        self.head = None
        self.tail = None


myCDLL = CircularDoublyLinkedList()
myCDLL.createCDLL(10)
print([i for i in myCDLL])
myCDLL.insertion(11, 0)
print([i for i in myCDLL])
myCDLL.insertion(12, 0)
print([i for i in myCDLL])
myCDLL.insertion(13, 0)
print([i for i in myCDLL])
myCDLL.insertion(9, -1)
print([i for i in myCDLL])
myCDLL.insertion(8, 5)
print([i for i in myCDLL])

myCDLL.traverse()

print("-----")
myCDLL.reverseTraversal()
print([i for i in myCDLL])
myCDLL.deletion(0)
print([i for i in myCDLL])

myCDLL.deletion(-1)
print([i for i in myCDLL])
myCDLL.deletion(1)
print([i for i in myCDLL])
