"""
Created on Sun Dec 10 14:01:40 2017
@author: Bruce
"""

from graphviz import Digraph

class BinaryTree:
    def __init__(self, root = None):
        '''Can create an empty tree'''
        self.root = root #Each child will be root of new tree
        self.leftChild = None
        self.rightChild = None
    
    def __repr__(self):
        return str(self.root)
    
    def getKey(self):
        return self.root
    
    def getLeft(self):
        return self.leftChild
    
    def getRight(self):
        return self.rightChild
    
    def numChildren(self): #Will be used for delete function cases
        if self.leftChild and self.rightChild:
            return 2
        elif self.leftChild or self.rightChild:
            return 1
        else:
            return 0
        
    def insert(self, newVal):
        ''' Insert a new value and its corresponding tree'''
        if self.root is None:
            self.root = newVal
        else:
            if newVal < self.root:
                if self.leftChild is None:
                    self.leftChild = BinaryTree(newVal)
                else:
                    self.leftChild.insert(newVal)
            elif newVal > self.root:
                if self.rightChild is None:
                    self.rightChild = BinaryTree(newVal)
                else:
                    self.rightChild.insert(newVal)
                
    def search(self, val):
        '''Search tree for a node with a matching key and return value or None'''
        if val < self.root:
            if self.leftChild is None:
                return None
            return self.leftChild.search(val) #Recursively search left sides
        elif val > self.root:
            if self.rightChild is None:
                return None
            return self.rightChild.search(val) #Recursively search right sides
        else:
            return self
            
    def parent(self, val):
        '''Find the parent node of input value, if value is not in tree, \
        then it tells you.'''
        if self.search(val) is None:
            return "Node is not in tree"
        # First check if either child node has the value, \
        #   if not then search recursively in the given direction (left/right)
        if self.leftChild != None and self.leftChild.root == val:
            return self
        elif self.rightChild != None and self.rightChild.root == val:
            return self
        elif val < self.root:
            return self.leftChild.parent(val)
        elif val > self.root:
            return self.rightChild.parent(val)
    
    #TODO Finish delete function
    def delete(self, val):
        '''Deletes and redirects node using one of three cases'''
        if self.search(val) is None:
            return "Node is not in tree"
        else:
            # Case 1: Node is a leaf :: set parent pointer to None
            if self.search(val).numChildren() == 0:
                if self.search(val).root < self.parent(val).root:
                    self.parent(val).leftChild = None
                elif self.search(val).root > self.parent(val).root:
                    self.parent(val).rightChild = None
            
            # Case 2: Node has exactly one child :: delete node and \ 
            #         set node's parent to point at child
            elif self.search(val).numChildren() == 1:
                if self.search(val).root < self.parent(val).root:
                    if self.search(val).leftChild is None:
                        self.parent(val).leftChild = self.search(val).rightChild
                    else:
                        self.parent(val).leftChild = self.search(val).leftChild
                elif self.search(val).root > self.parent(val).root:
                    if self.search(val).leftChild is None:
                        self.parent(val).rightChild = self.search(val).rightChild
                    else:
                        self.parent(val).rightChild = self.search(val).leftChild
            
            #Case 3: Node has 2+ children
            elif self.search(val).numChildren() == 2:
                nextNode = self.search(val).rightChild
                while nextNode.leftChild: #Loop until no more left child
                    parent = nextNode #Need to remamber the parent data
                    nextNode = nextNode.leftChild
                self.search(val).root = nextNode.root #Exchange values
                if parent.leftChild == nextNode: #Point the children correctly
                    parent.leftChild = nextNode.rightChild
                else:
                    parent.rightChild = nextNode.rightChild
    
    def traverse(self, order):
        '''Method to print values in tree depending on order requested'''
        
        if self.root != None: #Obv can't return value if None exists
            if order == "preorder":
                print(self.root)
                if self.leftChild:
                    self.leftChild.traverse("preorder")
                if self.rightChild:
                    self.rightChild.traverse("preorder")
            elif order == "inorder":
                if self.leftChild:
                    self.leftChild.traverse("inorder")
                print(self.root)
                if self.rightChild:
                    self.rightChild.traverse("inorder")
            elif order == "postorder":
                if self.leftChild:
                    self.leftChild.traverse("postorder")
                if self.rightChild:
                    self.rightChild.traverse("postorder")
                print(self.root)
            else: #In case someone puts in wrong input
                raise ValueError("Order must be either preorder, \
inorder, or postorder!")
    
    def buildEdges(self):
        '''Called to create list of nodes for arrows to be drawn between.
        Output is list and each set of 2 should be connected by an arrow'''
        if self.leftChild is None and self.rightChild is None: #Base case
            return []
        elif self.leftChild is None:
            return [self.root, self.rightChild.root] + self.rightChild.buildEdges()
        elif self.rightChild is None:
            return [self.root, self.leftChild.root] + self.leftChild.buildEdges()
        elif (self.leftChild is not None) and (self.rightChild is not None):
            return [self.root, self.leftChild.root, self.root, self.rightChild.root] \
                    + self.leftChild.buildEdges() + self.rightChild.buildEdges()
    
    #TODO Ensure arrows point correctly
        # Maybe add /None/ leaf?
    def visualize(self, outputPath):
        '''Method that uses graphviz/Digraph to make a visual representation\
        of our BST. Arrow are constructed using the buildEdges method.'''
        graph = Digraph(filename=outputPath) #Initiate the graphviz obj
        edges = self.buildEdges()
        for i in range(len(edges)): #Graphviz likes strings for edge names
            edges[i] = str(edges[i])
        for i in range(0, len(edges), 2): #Creates an arrow between every set of set elements
            graph.edge(edges[i], edges[i+1]) # E.g. [A, B, C, D] -> A->B, C->D
        graph.view()

    def height(self): # Used in the balance method
        '''Find height of tree at node X'''
        if self.leftChild == None:
            leftHeight = -1 #So that the "1 +" cancels to 0 at end
        else:
            leftHeight = self.leftChild.height()
        if self.rightChild == None:
            rightHeight = -1
        else:
            rightHeight = self.rightChild.height()
        return 1 + max(leftHeight, rightHeight)
    
    def balance(self, root): #Need to write this, probably using the preorder traverse method
        '''Check if every node is balanced or not by taking the difference \
        of the left tree height and right tree height: \
        bal(root) = leftChild.height() - rightChild.height() 
        and if not then re-sorts the tree to be balanced'''
        pass
    
    def rotation(tree, node, direction): #No idea so far
        pass
    
values = [10, 5, 7, 1, 15, 3, 6, 9, 8, 11]
for i in range(len(values)):
    if i == 0:
        root = BinaryTree(values[i])
    else:
        root.insert(values[i])

print(root.rightChild.height())

#root.traverse("inorder")
#root.visualize('roottest.gv')