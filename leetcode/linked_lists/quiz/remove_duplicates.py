"""
Write code to remove duplicates from an unsorted linked list
1. Use a temp set.
2. If in set, remove it, else go to the next next node
"""

from LinkedList import LinkedList


def removeDups(ll):
    if ll.head is None:
        return

    else:
        currentNode = ll.head
        visited = set([currentNode.val])
        while currentNode.next:
            if currentNode.next.val in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.val)
                currentNode = currentNode.next
    return ll


ll = LinkedList()
ll.generate(10, 5, 10)
print(ll)
print(removeDups(ll))
