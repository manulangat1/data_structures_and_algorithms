class Node: 
    def __init__(self, value = None):
        self.next = None 
        self.val = value
    # override the str method. 
    def __str__(self) -> str:
        return str( self.val)

class CircularLinkedList: 
    def __init__(self):
        self.head = None 
        self.tail = None

    # iter method. 
    def __iter__(self):
        # if not self.head: 

        #     return 
        node = self.head
        while node: 
            yield node.val
            if node == self.tail: 
                break
            node = node.next

    def insertion( self, value, posn): 
        """
            - 3 conditions: 
                1. At the start. 
                2. At any point. 
                3. At the end. 
        """
        newNode = Node(value)
        if posn == 0: 
            if not self.head:
                self.head = newNode
                self.tail = newNode
            else: 
                # point the new node next value to head
                # point the tail next node to the new node. 
                newNode.next = self.head 
                self.tail.next = newNode
                self.head = newNode
        elif posn == -1:
            newNode.next = self.head
            self.tail.next = newNode
            self.tail = newNode
        else: 
            tempNode = self.head 
            idx = 0 
            while idx < posn -1: 

                if tempNode.next == self.tail: 
                    break
                tempNode = tempNode.next 
                idx += 1 
            print(tempNode.val)
            nextNode = tempNode.next
            tempNode.next = newNode
            newNode.next = nextNode

    def traversal(self): 
        node = self.head
        while node: 
            print(node.val)
            if node == self.tail: 
                break
            node = node.next

    def search(self, searchItem): 
        node = self.head
        while node: 
            if node.val == searchItem: 
                return True
            if node == self.tail: 
                return False 
            node = node.next
        return False
            




        


myCSLL = CircularLinkedList()
node1 = Node(1)
node2 = Node(2)
myCSLL.head = node1
myCSLL.head.next = node2
myCSLL.tail = node2
myCSLL.tail.next = node1

print( [ i for i in myCSLL])
myCSLL.insertion(10,0)
print( [ i for i in myCSLL])
myCSLL.insertion(11,-1)
print( [ i for i in myCSLL])
myCSLL.insertion(11,2)
print( [ i for i in myCSLL])
myCSLL.insertion(12,1)
print( [ i for i in myCSLL])


print("------TRAVERSAL----")
myCSLL.traversal()

print(myCSLL.search(122))