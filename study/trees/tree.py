class TreeNode: 
    def __init__(self,data, children= None ):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children: 
            ret += child.__str__(level + 1)
        return ret
    
    def addChild( self, TreeNode): 
        self.children.append(TreeNode
                             )
        

tree = TreeNode("Drinks", [])
hot = TreeNode("Hot", [])
cold = TreeNode("Cold", [])
tree.addChild(hot)
tree.addChild(cold)
tea = TreeNode("Tea", [])
coffee = TreeNode("Coffee", [])
hot.addChild(tea)
hot.addChild(coffee)
print(tree)