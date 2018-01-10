# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 11:45:02 2018

@author: Bruce
"""
###############################################################################
# Exercise 01
###############################################################################

import time
from random import randint
import numpy as np

class pathRankSet:
    """
    Class that has set methods and uses union 
    by rank and find with path compression
    """
     
    def __init__(self):
        self.parent = {} #Create dictionaries for set assignments
        self.rank = {}
        
    def makeSet(self, x):
        self.parent[x] = x #Create dict entry for new node x
        self.rank[x] = 0
        
    def findSet(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.findSet(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.link(self.findSet(x), self.findSet(y))
        
    def link(self, x, y):
        if x == y: #In case they are in the same set already
            return
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
                
class noPathSet:
    """
    Class that has set methods and uses union 
    by rank and find with path compression
    """
     
    def __init__(self):
        self.parent = {} #Create dictionaries for set assignments
        self.rank = {}
        
    def makeSet(self, x):
        self.parent[x] = x #Create dict entry for new node x
        self.rank[x] = 0
        
    def findSet(self, x):
        if x != self.parent[x]:
            # TODO modify findSet and remove path compression
            # Running into recursion problem
            self.parent[x] = self.findSet(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.link(self.findSet(x), self.findSet(y))
        
    def link(self, x, y):
        if x == y: #In case they are in the same set already
            return
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

def time_set_func(set_class, it=10, num_sets=1000, num_op = 500000):
    times=[]
    dset = set_class()
    t=[]
    for i in range(it):
	    # Time the function
        tStart=time.time()
        for n in range(1, num_sets+1):
            dset.makeSet(n)
        for op in range(num_op):
            coin_toss = randint(0, 1)
            if coin_toss == 0:
                dset.findSet(randint(1, num_sets))
            else:
                dset.union(randint(1, num_sets), randint(1, num_sets))
        tEnd=time.time()
        t.append(tEnd-tStart)
    avgTime=np.average(np.asarray(t))
    times.append(avgTime)
    return times
                
#print(time_set_func(noPathSet))
dset = pathRankSet()
dset.makeSet('a')
dset.makeSet('b')
dset.union('a', 'b')

###############################################################################
# Exercise 02
###############################################################################

class pathRankSet:
    """
    Class that has set methods and uses union 
    by rank and find with path compression
    """
     
    def __init__(self):
        self.parent = {} #Create dictionaries for set assignments
        self.rank = {}
        
    def makeSet(self, x):
        self.parent[x] = x #Create dict entry for new node x
        self.rank[x] = 0
        
    def findSet(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.findSet(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.link(self.findSet(x), self.findSet(y))
        
    def link(self, x, y):
        if x == y: #In case they are in the same set already
            return
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

class Graph:
    """
    Class that generates nodes and edges between them, while retaining
    the weights of edges.
    """
    
    def __init__(self):
        self.nodes = set() # sets can't have duplicates
        self.edges = dict() # assign nodes with edges
        self.weights = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value]=[] #Add dict element -> node : [edges]
    
    def add_edge(self, from_node, to_node, weight = 1):
        self.weight = weight #Default it to 1
        if(not from_node in self.edges.keys()): 
            self.edges[from_node]=[]
        
        if(not to_node in self.edges.keys()):
            self.edges[to_node]=[]
        self.edges[from_node].append(to_node) #Add to_node vlaue to node's edge list
        self.edges[to_node].append(from_node) # This is for undirected graph
        self.weights[(from_node, to_node)] = weight
        
    def getNodes(self):
        return list(self.nodes)

def dfs(graph, start):
    '''Depth First Search function'''
    visited, stack = set(), [start]
    vl=[]
    while stack:
        vertex = stack.pop() # Get element from the end
        if vertex not in visited:
            visited.add(vertex)
            vl.append(vertex)
            #print(graph.weights) for testing
            stack.extend(set(graph.edges[vertex]) - visited)# Add elements to the end
    return vl

def mst(graph):
    '''
    Function that finds the Minimum Spanning Tree of a connected graph
    given that the edges have weights
    '''
    graph_nodes = graph.getNodes()
    connected_nodes = dfs(graph, graph_nodes[0])
    for vertex in graph_nodes:
        assert vertex in connected_nodes #Check if graph is connected
    paths = [] #List of MST edges
    node_set = pathRankSet() #Create set environment
    for node in graph_nodes: #Convert nodes into sets
        node_set.makeSet(node)
    #Sort by weights (values in dict)
    sorted_edges_weights = sorted(graph.weights.items(), key = lambda x: (x[1], x[0])) 
    sorted_edges = []
    for edge in sorted_edges_weights:
        sorted_edges.append(list(edge[0]))
    for pair in sorted_edges:
        #If two nodes aren't in the same tree, then add them to list
        if node_set.findSet(pair[0]) != node_set.findSet(pair[1]):
            paths.append(pair)
            node_set.union(pair[0], pair[1])
    return paths

g=Graph()
g.add_node('a')
g.add_node('b')
g.add_node('c')
g.add_node('d')
g.add_node('e')

g.add_edge('a','b', 1)
g.add_edge('a','c', 3)
g.add_edge('a','e', 4)
g.add_edge('b','d', 4)
g.add_edge('b','c', 2)
g.add_edge('c','d', 4)
g.add_edge('b','e', 5)
g.add_edge('d','e', 2)

print(mst(g))

