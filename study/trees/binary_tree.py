"""
Docstring for study.trees.binary_tree
- Each node has at most 2 children. 
- Is a family of data structures  that are used to represent hierachial data. ( BST, Heap tree, ACL, red balck trees, Syntax trees)

Why?
- Fast search, insertion and deletion.
- Prereq for many advanced trees. 

Types of Binary Trees: 
1. Perfect Binary Tree: Every level is completely filled except last node and it has all levels as left as possible.
2. Full Binary Tree: Every node has either 0 or 2 children.
3. Complete Binary Tree: Every level is completely filled except possibly the last level, which is filled from left to right.
4. Balanced Binary Tree: The difference in height between the left and right subtrees of any node is at most one.
5. Degenerate (or pathological) Binary Tree: Each parent node has only one child, making the tree essentially a linked list.
"""
from collections import deque

class BinaryTreeNode: 
    def __init__(self, data ):
        self.data = data 
        self.leftChild = None 
        self.rightChild = None 

newBT = BinaryTreeNode("Drinks")
cold = BinaryTreeNode("Cold")
hot = BinaryTreeNode("Hot")
newBT.leftChild = cold
newBT.rightChild = hot

#  2 main traversal methods:
"""

 2 main traversal methods:
    1. Depth First Traversal. 
        - Pre order traversal: Root, left, right 
        - IN order traversal: Left, root, right. 
        - Post order traversal: Left, right, root. 
        - Time and space complexity: 0(n) where n is the number of nodes in the tree.
    2. Breadth First Traversal: 
        - Level order traversal: Traverse the tree level by level from left to right. 
"""

def preOrderTraversal(root): 
    if not root:
        return 
    print(root.data)
    preOrderTraversal(root.leftChild)
    preOrderTraversal(root.rightChild)

def inOrderTraversal(root): 
    if not root:
        return 
    inOrderTraversal (root.leftChild)
    print(root.data)
    inOrderTraversal(root.rightChild)

def postOrderTraversal(root): 
    if not root:
        return 
    postOrderTraversal(root.leftChild)
    postOrderTraversal(root.rightChild)
    print(root.data)

print("Pre order traversal")
preOrderTraversal(newBT)
print("In order traversal")
inOrderTraversal(newBT)
print("Post order traversal")
postOrderTraversal(newBT)
print("End of traversal")

"""
level order traversal: 
    - use a queue to keep track of the nodes at each level.
    - Time complexity: 0 (n) where n is the number of nodes in the tree. 
"""
def levelOrderTraversal(root): 
    if not root: 
        return
    queue = [ root]
    while queue: 
        currentNode = queue.pop(0)
        print(currentNode.data)
        if currentNode.leftChild:
            queue.append(currentNode.leftChild)
        if currentNode.rightChild:
            queue.append(currentNode.rightChild)
print("Level order traversal")
levelOrderTraversal(newBT)

# searching for an element in a binary tree: 
def search(root, searchItem): 
    """
    Docstring for search
    
    :param root: Description
    :param searchItem: Description
    recursion method!
    """
    if not root:
        return False
    if root.data == searchItem: 
        return True
    return search( root.leftChild, searchItem) or search(root.rightChild, searchItem)

def searchIterative(root, searchItem):
    if not root:
        return False
    queue = [ root]
    while queue: 
        currentNode = queue.pop(0)
        if currentNode.data == searchItem: 
            return True
        if currentNode.leftChild:
            queue.append(currentNode.leftChild)
        if currentNode.rightChild:
            queue.append(currentNode.rightChild)
    return False

def insertion(root, newData): 
    """
    Docstring for insertion
    
    :param root: Description
    :param newData: Description
    2 edge cases. 
    1. If the tree is empty, we can simply create a new node and set it as the root of the tree.
    2. If tree is not empty, use the  level order traversal to find the first vacant spot in the tree and insert the new node there.
    """
    if root is None:
        root = BinaryTreeNode(newData)
        return root 
    
    queue = deque([root])
    while queue: 
        currentNode = queue.popleft()
        if currentNode.leftChild is None:
            currentNode.leftChild = BinaryTreeNode( newData)
            return root
        else: 
            queue.append(currentNode.leftChild )
        if currentNode.rightChild is None: 
            currentNode.rightChild = BinaryTreeNode( newData)
            return root
        else: 
            queue.append( currentNode.rightChild) 




newBTA =insertion( newBT, "Soda")
print(newBTA)
levelOrderTraversal(newBT)
    

def getDeepestNode(root): 
    if not root:
        return None 
    queue = deque([ root])
    while queue: 
        current = queue.popleft()
        if current.leftChild: 
            queue.append(current.leftChild)
        if current.rightChild: 
            queue.append(current.rightChild)  
    deepestNode = root.data
    return deepestNode

def deleteDeepestNode( root,  deepestNode): 
    """
    1. Find the deepest node. 
    2. Find the node to be deleted. 
    3. Replace the node to be deleted with the deepest node. 
    4. Delete the deepest node.
    """
    if not root:
        return None 
    
    queue = deque([root])
    while queue: 
        current = queue.popleft()
        if current.data == deepestNode: 
            current.value = None 
            return
        if current.rightChild:
            if current.rightChild is deepestNode: 
                current.rightChild = None 
            else: 
                queue.append(current.rightChild)

        if current.leftChild:
            if current.leftChild is deepestNode: 
                current.leftChild = None 
            else: 
                queue.append(current.leftChild)

print("get deepestNode", getDeepestNode( newBT))
deepestNode = getDeepestNode( newBT)
print("deepest node", deepestNode)