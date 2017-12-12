# -*- coding: utf-8 -*-
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
    
    def getRoot(self):
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
        '''Search tree for a node with a matching key and return True/False'''
        if val < self.root:
            if self.leftChild is None:
                return "Element is not in tree"
            return self.leftChild.search(val) #Recursively search left sides
        elif val > self.root:
            if self.rightChild is None:
                return "Element is not in tree"
            return self.rightChild.search(val) #Recursively search right sides
        else:
            return True
            
    #TODO Finish delete function
    # How to look at node before??
    def delete(self, val):
        if self.search(val) is True:
            if self.numChildren(val) == 0:
                return self.root

    
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
        graph = Digraph(filename=outputPath) #Initiate the graphviz obj
        edges = self.buildEdges()
        for i in range(len(edges)): #Graphviz likes strings for edge names
            edges[i] = str(edges[i])
        for i in range(0, len(edges), 2): #Creates an arrow between every set of set elements
            graph.edge(edges[i], edges[i+1]) # E.g. [A, B, C, D] -> A->B, C->D
        graph.view()

    
values = [10, 5, 7, 1, 15, 3, 6, 9, 8, 11]
for i in range(len(values)):
    if i == 0:
        root = BinaryTree(values[i])
    else:
        root.insert(values[i])

root.visualize('roottest.gv')

