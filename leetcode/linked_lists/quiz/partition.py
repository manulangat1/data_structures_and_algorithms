""" """

from LinkedList import LinkedList


def partition(ll, x):

    if ll.head is None:
        return

    beforeHead = before = None
    afterHead = after = None

    currNode = ll.head
    while currNode:
        nextNode = currNode.next
        currNode.next = None
        if currNode.val < x:
            if beforeHead is None:
                beforeHead = before = currNode
            else:
                before.next = currNode
                before = currNode
        else:
            if afterHead is None:
                afterHead = after = currNode
            else:
                after.next = currNode
                after = currNode
        currNode = nextNode

    # merge the two lists
    if beforeHead is None:
        ll.head = afterHead
        return

    before.next = afterHead
    ll.head = beforeHead
    return ll


ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(partition(ll, 50))
