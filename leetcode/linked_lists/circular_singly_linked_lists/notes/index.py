"""
Last node points to the first node of the linked list. 
"""
class ListNode: 
    def __init__(self, value = None, next = None ):
        self.val = value
        self.next = next


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None

    def __iter__(self):
        if self.head is None:
            return
        current = self.head 
        while True: 
            yield current.val
            current = current.next 

            if current == self.head:
                break
        # head = self.head 
        # while head:
        #     yield head.val
        #     head = head.next 

        #     if head == self.tail.next:
        #         break

    def insertion(self, value, posn):
        """
        3 condition:
            1. At the start of the list. 
            2. At the end of the list. 
            3. At any posn on the list. 
        """
        newNode = ListNode(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = newNode
        else: 
            if posn == 0 : 
                if self.head is None: 
                    self.head = newNode
                    self.tail = newNode
                    self.tail.next = newNode
                else: 
                    newNode.next = self.head 
                    self.head = newNode
                    self.tail.next = newNode
            elif posn == -1:
                newNode.next = self.head
                self.tail.next = newNode
                self.tail = newNode
            else: 
                count = 0 
                tempNode = self.head 
                while count < posn -1: 
                    tempNode = tempNode.next 
                    count += 1 
                nextNode = tempNode.next 
                tempNode.next = newNode
                newNode.next = nextNode

                if tempNode == self.tail: 
                    self.tail = newNode
                    self.tail.next = self.head

    def traversal( self): 
        """
        time complexity is 0(n) while space complexity is 0(1)
        """
        if self.head is None: return
        head = self.head 
        count = 0 
        while head: 
            print( "*" * count  , head.val)
            head = head.next
            count += 1

            if head == self.head:
                break
    def search(self, value):
        """
        time complexity is 0(n) while space complexity is 0(1)
        """
        if self.head is None: 
            return None 
        else: 
            head = self.head 
            while head: 
                if head.val == value:
                    return head
                head = head.next
                if head == self.head:
                    break
        return None
    
    def deletion(self, posn): 
        """
        3 scenarios. 
        1. At the start of the CSLL. 
        2. At the end of the list. 
        3. At any posn in the list. 
        """
        if self.head is None:
            return
        if self.head == self.tail: 
            self.head = None 
            self.tail = None
        
        else: 
            if posn == 0 : 
                if self.head == self.tail:

                    self.head = None 
                    self.tail = None
                else: 
                    self.head = self.head.next 
                    self.tail.next = self.head 
            elif posn == -1: 
                tempNode = self.head 
                while tempNode.next != self.tail:
                    tempNode = tempNode.next  
                tempNode.next = self.head
                self.tail = tempNode
            else: 
                count, tempNode  = 0 , self.head 
                while count < posn -1 : 
                    tempNode = tempNode.next 
                    count += 1 
                tempNode.next = tempNode.next.next

    def deleteEntireCSLL( self):
        self.head = None 
        self.tail = None




    


CSLL = CircularSinglyLinkedList()
print([ i for i in CSLL])
CSLL.insertion(5,0)
print([ i for i in CSLL])
CSLL.insertion(6,0)
print([ i for i in CSLL])
CSLL.insertion(7,0)
print([ i for i in CSLL])
CSLL.insertion(8,0)
print([ i for i in CSLL])
CSLL.insertion(9,-1)
print([ i for i in CSLL])
CSLL.insertion(71,5)
print([ i for i in CSLL])

CSLL.traversal()

# for _ in range(5):

#     CSLL.deletion(1)
#     print([ i for i in CSLL])
CSLL.deleteEntireCSLL()
print([ i for i in CSLL])