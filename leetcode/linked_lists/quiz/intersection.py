"""
Get an intersection of two lists.
"""

from LinkedList import LinkedList, Node


def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)

    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    return longerNode


ll = LinkedList()
llB = LinkedList()
ll.add(50)
ll.add(10)
ll.add(40)
ll.add(60)

llB.add(50)
llB.add(500)
llB.add(10)
llB.add(40)
llB.add(60)

print(ll)
print(intersection(ll, llB))
