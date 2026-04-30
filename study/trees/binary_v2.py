"""
Binary tree -
    * DS in which each node has at most 2 children i.e left and right child.
    * Is a family of data structures. ( BST, Heap tree, AVL , red black tree, syntax tree. )

Types of BT.
    1. Full binary.
    2. Perfect bt. - all nodes at same level and have 2 children.
    3 Complete BT - all levels are filled except last possible level.
    4. Balanced BT - each leaf is not more than a certain distance than another one.
"""

from collections import deque
from ..space import random_spacing


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


def preOrderTraversal(root):
    print(root.leftChild)
    print(root.data)
    print(root.rightChild)


def inOrderTraversal(root):
    print(root.data)
    print(root.leftChild)
    print(root.rightChild)


def postOrderTraversal(root):
    print(root.leftChild)
    print(root.rightChild)
    print(root.data)


def levelOrderTraversal(root):
    if not root:
        return
    customQ = []
    customQ.append(root)

    while customQ:
        root = customQ.pop(0)
        print(root.data)

        if root.leftChild:
            customQ.append(root.leftChild)
        if root.rightChild:
            customQ.append(root.rightChild)


def search(root, searchItem):
    if not root:
        return

    customQ = [root]

    while customQ:
        root = customQ.pop(0)
        if root == searchItem:
            return True
        if root.leftChild:
            customQ.append(root.leftChild)
        if root.rightChild:
            customQ.append(root.rightChild)
    return False


def insert(root, newNode):
    if not root:
        root = newNode
    else:
        customQ = [root]

        while customQ:
            node = customQ.pop(0)
            if node.leftChild is not None:
                customQ.append(node.leftChild)
            else:
                node.leftChild = newNode
            if node.rightChild is not None:
                customQ.append(node.rightChild)
            else:
                node.rightChild = newNode


def getDeepestNode(root):
    if not root:
        return
    q = [root]
    while q:
        current = q.pop(0)
        if current.leftChild:
            q.append(current.leftChild)
        if current.rightChild:
            q.append(current.rightChild)
    deepestNode = root.data
    return deepestNode


def deleteDeepestNode(root, deepestNode):
    if not root:
        return
    q = [root]
    while q:
        current = q.pop(0)
        if current.data == deepestNode:
            current.value = None
            return
        if current.rightChild:
            if current.rightChild is deepestNode:
                current.rightChild = None
            else:
                q.append(current.rightChild)

        if current.leftChild:
            if current.leftChild is deepestNode:
                current.leftChild = None
            else:
                q.append(current.leftChild)


def deleteNode(root, node):
    if not root:
        return
    q = [root]
    while q:
        current = q.pop(0)
        if current == node:
            dNode = getDeepestNode(root)
            root.data = dNode.data
            deleteDeepestNode(root, dNode)
            return True
        if current.leftChild:
            q.append(current.leftChild)
        if current.rightChild:
            q.append(current.rightChild)
    return False


newBT = TreeNode("Drinks")
cold = TreeNode("Cold")
hot = TreeNode("Hot")
newBT.leftChild = cold
newBT.rightChild = hot


print("Pre order traversal")
preOrderTraversal(newBT)
print("In order traversal")
inOrderTraversal(newBT)
print("Post order traversal")
postOrderTraversal(newBT)
print("End of traversal")
random_spacing()
levelOrderTraversal(newBT)
random_spacing()
print(search(newBT, "Tea"))

insert(newBT, "Tea")
print(search(newBT, "Tea"))
