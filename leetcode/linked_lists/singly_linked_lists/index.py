class ListNode: 
    def __init__(self, val= None):
        self.val = val 
        self.next = None 
    def __str__(self):
        return str(self.val)


class SinglyLinkedList: 
    def __init__(self):
        self.head = None 
        self.tail = None 

    def __iter__(self):
        head = self.head 
        while head: 
            yield head.val 
            head = head.next 
    

    def __self__(self): 
        head = self.head
        while head: 
            print(head.val)
            head = head.next 

    def insertion(self, value, posn): 
        """
        time and space complexity is 0(1 ) for all the cases.
        """
        if not self.head: 
            newNode = ListNode()
            newNode.val = value 
            self.head = newNode 
            self.tail = newNode 
        else: 
            if posn == 0 :
                newNode = ListNode(value)
                newNode.next = self.head 
                self.head = newNode 
            elif posn == -1:
                newNode = ListNode(value)
                self.tail.next = newNode
                self.tail = newNode 
            else: 
                newNode = ListNode(value)
                count = 0 
                tempNode = self.head 
                while count < posn -1: 
                    if tempNode.next:
                        tempNode = tempNode.next 
                        count += 1 
                    else: 
                        break
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail: 
                    self.tail = newNode

    def traversal(self): 
        # time complexity is 0(n ) while space complexity is 0(1)
        head = self.head 
        step = 0 
        while head: 
            print( " " * step , head.val)
            head = head.next 
            step += 1 

    def search( self, value): 
        # space complexity is 0(1) while time complexity is 0(n)
        if self.head is None: 
            return None 
        else: 
            head = self.head 
            while head: 
                if head.val == value:
                    return head
                head = head.next
        return None
    
    def deletion(self, posn): 
        """
        Time complexity is 0(n) while space complexity is 0(1)
        1. At the start of the list. 
        2. Any posn in the list. 
        3. At the end of the list. 
        """

        if self.head is None: return
        if posn == 0: 
            if self.head == self.tail:
                self.head = None 
                self.tail = None
            else: 
                self.head = self.head.next 
        elif posn == -1:
            tempNode = self.head 
            while tempNode: 
                if tempNode.next == self.tail: 
                    tempNode.next = None 
                    self.tail = tempNode
                    return
                tempNode = tempNode.next 
        else: 
            count = 0 
            tempNode = self.head 
            while count < posn -1:
                if tempNode.next:
                    tempNode = tempNode.next 
                    count += 1
                else:
                    return
            tempNode.next = tempNode.next.next 

        pass
SLL = SinglyLinkedList()
SLL.insertion(1,0)
SLL.insertion(2,0)
SLL.insertion(3,0)
SLL.insertion(4,1)
print([ head for head in SLL])
SLL.traversal()
print(SLL.search(3))
SLL.deletion(0)
print([ head for head in SLL])
SLL.deletion(-1)
print([ head for head in SLL])
SLL.deletion(1)
print([ head for head in SLL])