#!/usr/bin/python

#Class for Vertex
class Vertex:
    def __init__(self, ID, X, Y):
        self.ID = int(ID)
        self.X = int(X)
        self.Y = int(Y)

    def get_coordinate(self):
	return [self.X, self.Y]


#Class for Edge
class Edge:
    def __init__(self, ID, V1, V2):
        self.ID = int(ID)
        self.V1 = int(V1)
        self.V2 = int(V2)

#Class for Node
class Node:
    def __init__(self, index, parent = None):
	self.index = index
	self.parent = parent
	self.depth = -1
	self.heur = 0.0
	self.successor = []
	self.tracebacks = []
	
    def successors(self):
	return self.successor
    def traceback(self):
	return self.tracebacks

class GlobalVariable:
	debug = 0

 
