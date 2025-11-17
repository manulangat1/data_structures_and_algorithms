"""
- Is a list of sequential collection and does not have to be in order. 
- Made up of independent nodes that may contain any type of data and each node has a reference to the next node in the link.

Linked Lists vs Arrays:
    - Elements of a linked list are independent objects. 
    - Variable size - size of a linked list is not predefined. 
    - Insertion and removals in Linked lIst are very efficient. 
    - Random access of an element is very efficient in arrays. 

Types of Linked List: 
    - Singly Linked List. 
        - Each node in the list stores the value and ref to the next node in the list.
        - The ref to the first and last nodes in the list is null. 
    - Circular Singly Linked List. 
        - Each node in the list has the value and ref to the next node in the list.
        - Last node has ref to the first node. 
    - Doubly linked list. 
        - Each node has value and ref to the prev and next nodes in the list. 
    - Circular doubly linked list. 
        - Each node has value and ref to the prev and next node in the list. 
        - First node has ref to the prev node. 
        - Last node has ref to the first node. 
"""

class Node:
    def __init__(self, value= None):
        # self.head = None 
        self.val = value
        self.next = None 

    def __str__(self):
        return str( self.val)


class SLinkedList: 
    def __init__(self):
        self.head = None 
        self.tail = None

    def __iter__(self): 
        head = self.head 
        while head: 
            yield head.val
            head = head.next 

    def insertion( self, value , posn):
        """
        - 3 scenarios: 
            - At the beginning of the linked list. 
            - At the middle of the linked list. 
            - At the end of the linked list
        Edge cases to be handled:
            1. If the list is empty.
        """
        new_node = Node(value)
        if not self.head: 
            self.head = new_node
            self.tail = new_node
        if posn == 0: 
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else: 
                # update the new node next to point to the current head. 
                # move the 
                new_node.next = self.head
                self.head = new_node
        elif posn == -1: 
            if not self.head: 
                self.head = new_node
                self.tail = new_node
            else: 
                #  assign the tail next ref to the new node. 
                # make the new node to be the tail. 
                #  Link established. 
                self.tail.next = new_node
                self.tail = new_node

        else: 
            # loop till posn -1 
            # have the next to be next to be the new node. 
            """
            Edge case to consider: 
                1. If the new node to be added is the tail. 
            """
            counter = 0 
            tempNode = self.head
            while counter < posn -1 : 
                print( self.head)
                if self.head.next: 
                    tempNode = tempNode.next
                    counter += 1 
                else: 
                    break
            print(tempNode.val , " at posn", posn, counter)
            nextNode = tempNode.next 
            tempNode.next = new_node
            new_node.next = nextNode

            if tempNode == self.tail: 
                self.tail = tempNode
       

    def traversal(self): 
        """
        time complexity is 0(n)
        space complexity is O(1)
        """
        node = self.head
        while node: 
            print( node)
            node = node.next

    def search(self, searchItem): 
        

        node = self.head
        while node: 
            if node.val == searchItem: 
                return "Found at {0}".format( node)
            else: 
                node = node.next
        return "Not found"
    
    def deletion ( self, posn): 
        """
            - 3 conditions:
                - 1. Delete the first node. 
                - 2. Delete at any posn. 
                - 3. Delete the last node.
        """
        if self.head is None: 
            return 
        
        if posn == 0 : 
            # check whether the node is the only one in the list. 
            if self.head == self.tail: 
                self.head = None 
                self.tail = None 
            else: 
                self.head = self.head.next
        elif posn == -1: 
            tempNode = self.head
            while tempNode: 
                if  tempNode.next == self.tail:
                    break
                tempNode = tempNode.next
            tempNode.next = None
            self.tail = tempNode
        else: 
            
            idx = 0 
            tempNode =self.head
            while idx < posn -1: 
                tempNode = tempNode.next 
                idx += 1 
            tempNode.next = tempNode.next.next
    

    def deleteEntireSLL(self): 
        self.head = None 
        self.tail = None
        



    

SLL = SLinkedList()
node1 = Node(1)
node2 = Node(2)
SLL.head = node1
node1.next = node2
SLL.tail = node2

print( [ head for head in SLL])

SLL.insertion(10,0)

print( [ head for head in SLL])

SLL.insertion(100,0)

print( [ head for head in SLL])
SLL.insertion(1000,-1)

print( [ head for head in SLL])
SLL.insertion(20, 2)
print( [ head for head in SLL])

# SLL.insertion(20, 60)
# print( [ head for head in SLL])

print("------TRAVERSAL----")
SLL.traversal()

print("------SEARCH----")
print(SLL.search(100))
print( [ head for head in SLL])
SLL.deletion(0)
print( [ head for head in SLL])

SLL.deletion(-1)
print( [ head for head in SLL])


SLL.deletion(1)
print( [ head for head in SLL])

SLL.deleteEntireSLL()
print( [ head for head in SLL])