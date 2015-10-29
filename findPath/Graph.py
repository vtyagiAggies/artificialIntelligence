#!/usr/bin/python
import sys
import math
from Nodes import Node
from Nodes import Vertex
from Nodes import Edge
from Nodes import GlobalVariable

#Class for Graph
class Graph:
    def __init__(self, filepath):
	try:
		file = open(filepath)
	except:
		print "%s: file doesn't exist"%(filepath)
		sys.exit()
	lines = [line.rstrip('\n') for line in file.readlines()]
	self.verticies = [None]*275
	self.edges = [None]*641
	self.nodes = []
	#Getting list of all Vertex
	for line in lines[1:276]:
		entities = line.split(' ')
		self.verticies[int(entities[0])] = Vertex(entities[0], entities[1], entities[2])
	
	#Getting list of all Edges
	for line in lines[277:]:
		entities = line.split(' ')
		self.edges[int(entities[0])] = Edge(entities[0], entities[1], entities[2])
	
	#Getting list of all Nodes
	for vertex in self.verticies:
		self.nodes.append(Node(vertex.ID))
		for edge in self.edges: 
			if(vertex.ID == edge.V1):
				self.nodes[vertex.ID].successor.append(edge.V2)
			if(vertex.ID == edge.V2):
				self.nodes[vertex.ID].successor.append(edge.V1)
	self.debug = GlobalVariable.debug 
 
    #Breadth-First-Search
    def BFS_Search(self,initial_state, goal):
	queue = []
	depth = 0
	i = 0 #total iterations
	max = 0 #Maximum frontier size
	v = 0 #verices visited
	if self.debug == 1:
		print "Vertices=%d, edges=%d"%(len(self.verticies), len(self.edges))
		print "Start=(%d,%d), goal=(%d,%d), vertices: %d and %d"%(self.verticies[initial_state.index].X, self.verticies[initial_state.index].Y, self.verticies[goal.index].X, self.verticies[goal.index].Y, self.verticies[initial_state.index].ID, self.verticies[goal.index].ID) 
	queue.append(initial_state.index)
	self.nodes[initial_state.index].depth = 0 #Start node
	while queue:
		curr = queue[0]; queue = queue[1:] #equivalent to takine first element from queue
		
		
		i += 1
		if self.debug==1 :
			dist2goal = math.sqrt(math.pow(self.verticies[curr].X - self.verticies[goal.index].X ,2) + math.pow(self.verticies[curr].Y - self.verticies[goal.index].Y,2))
			print "iter=%d, frontier=%d, popped=%d (%d,%d), depth=%d, dist2goal=%.1f"%(i,len(queue),curr, self.verticies[curr].X, self.verticies[curr].Y, self.nodes[curr].depth, dist2goal)
		if(curr == goal.index):
			self.nodes[curr].tracebacks = [initial_state.index] + self.nodes[curr].tracebacks			
			return self.nodes[curr].tracebacks, v, i, max
			break
		for x in self.nodes[curr].successors():
			if self.nodes[x].depth == -1 :     #if index not visited
				queue.append(x)
				self.nodes[x].parent = self.nodes[curr]
				self.nodes[x].depth =  self.nodes[curr].depth + 1 
				self.nodes[x].tracebacks = self.nodes[curr].tracebacks + [x]
				v += 1
				if self.debug==1 :
					print "pushed %d (%d,%d)"%(x, self.verticies[x].X, self.verticies[x].Y)
		if len(queue) > max:
			max = len(queue)	
	
    #Depth-First-Search
    def DFS_Search(self,initial_state, goal):
	stack = []
 	depth = 0
	i = 0 #total iterations
	max = 0 #Maximum frontier size
	v = 0 #verices visited
	if self.debug == 1:
		print "Vertices=%d, edges=%d"%(len(self.verticies), len(self.edges))
		print "Start=(%d,%d), goal=(%d,%d), vertices: %d and %d"%(self.verticies[initial_state.index].X, self.verticies[initial_state.index].Y, self.verticies[goal.index].X, self.verticies[goal.index].Y, self.verticies[initial_state.index].ID, self.verticies[goal.index].ID) 
	stack.append(initial_state.index)
	self.nodes[initial_state.index].depth = 0 #Start node
	while stack:
		curr = stack[-1]; stack = stack[:-1] #equivalent to takine last element from stack
	
		if(curr == goal.index):
			self.nodes[curr].tracebacks = [initial_state.index] + self.nodes[curr].tracebacks			
			return self.nodes[curr].tracebacks, v, i, max
			break
		i += 1
		if self.debug==1 :
			dist2goal = math.sqrt(math.pow(self.verticies[curr].X - self.verticies[goal.index].X ,2) + math.pow(self.verticies[curr].Y - self.verticies[goal.index].Y,2))
			print "iter=%d, frontier=%d, popped=%d (%d,%d), depth=%d, dist2goal=%.1f"%(i,len(stack),curr, self.verticies[curr].X, self.verticies[curr].Y, self.nodes[curr].depth, dist2goal)
		for x in self.nodes[curr].successors():
			if self.nodes[x].depth == -1 :     #if index not visited
				stack.append(x)
				self.nodes[x].parent = self.nodes[curr]
				self.nodes[x].depth =  self.nodes[curr].depth + 1 
				self.nodes[x].tracebacks = self.nodes[curr].tracebacks + [x]
				v += 1
				if self.debug==1 :
					print "pushed %d (%d,%d)"%(x, self.verticies[x].X, self.verticies[x].Y)
		if len(stack) > max:
			max = len(stack)


    #Greedy-Best-First-Search
    def GBFS_Search(self,initial_state, goal):
	queue = {}          #queue having heuristic and index value so that index having best heuristic value can be selected
	depth = 0
	i = 0 #total iterations
	max = 0 #Maximum frontier size
	v = 0 #verices visited
	if self.debug == 1:
		print "Vertices=%d, edges=%d"%(len(self.verticies), len(self.edges))
		print "Start=(%d,%d), goal=(%d,%d), vertices: %d and %d"%(self.verticies[initial_state.index].X, self.verticies[initial_state.index].Y, self.verticies[goal.index].X, self.verticies[goal.index].Y, self.verticies[initial_state.index].ID, self.verticies[goal.index].ID) 
	queue[initial_state.index] = math.sqrt(math.pow(self.verticies[initial_state.index].X - self.verticies[goal.index].X ,2) + math.pow(self.verticies[initial_state.index].Y - self.verticies[goal.index].Y,2))
	self.nodes[initial_state.index].depth = 0 #Start node
	while queue:
		
		curr = sorted(queue, key = queue.get)[0]
		del queue[curr] 		
		if(curr == goal.index):
			self.nodes[curr].tracebacks = [initial_state.index] + self.nodes[curr].tracebacks		
			return self.nodes[curr].tracebacks, v, i, max
			break
		i += 1	
		if self.debug==1 :
			dist2goal = math.sqrt(math.pow(self.verticies[curr].X - self.verticies[goal.index].X ,2) + math.pow(self.verticies[curr].Y - self.verticies[goal.index].Y,2))
			print "iter=%d, frontier=%d, popped=%d (%d,%d), depth=%d, dist2goal=%.1f"%(i,len(queue),curr, self.verticies[curr].X, self.verticies[curr].Y, self.nodes[curr].depth, dist2goal)
		for x in self.nodes[curr].successors():
			if self.nodes[x].depth == -1 :     #if index not visited
				self.nodes[x].parent = self.nodes[curr]
				self.nodes[x].depth =  self.nodes[curr].depth + 1 
				self.nodes[x].heur = math.sqrt(math.pow(self.verticies[x].X - self.verticies[goal.index].X ,2) + math.pow(self.verticies[x].Y - self.verticies[goal.index].Y,2))
				queue[x] = self.nodes[x].heur
				self.nodes[x].tracebacks = self.nodes[curr].tracebacks + [x]
				v += 1
				if self.debug==1 :
					print "pushed %d (%d,%d)"%(x, self.verticies[x].X, self.verticies[x].Y)
		if len(queue) > max:
			max = len(queue)
		
 #ASTAR-Search
    def ASTAR_Search(self,initial_state, goal):
	queue = {}          #queue having heuristic and index value so that index having best heuristic value can be selected
	depth = 0
	i = 0 #total iterations
	max = 0 #Maximum frontier size
	v = 0 #verices visited
	if self.debug == 1:
		print "Vertices=%d, edges=%d"%(len(self.verticies), len(self.edges))
		print "Start=(%d,%d), goal=(%d,%d), vertices: %d and %d"%(self.verticies[initial_state.index].X, self.verticies[initial_state.index].Y, self.verticies[goal.index].X, self.verticies[goal.index].Y, self.verticies[initial_state.index].ID, self.verticies[goal.index].ID) 
	queue[initial_state.index] = math.sqrt(math.pow(self.verticies[initial_state.index].X - self.verticies[goal.index].X ,2) + math.pow(self.verticies[initial_state.index].Y - self.verticies[goal.index].Y,2))
	self.nodes[initial_state.index].depth = 0 #Start node
	while queue:
		
		curr = sorted(queue, key = queue.get)[0]
		del queue[curr]
		if(curr == goal.index):
			self.nodes[curr].tracebacks = [initial_state.index] + self.nodes[curr].tracebacks		
			return self.nodes[curr].tracebacks, v, i, max
			break
		i += 1	
		if self.debug==1 :
			dist2goal = math.sqrt(math.pow(self.verticies[curr].X - self.verticies[goal.index].X ,2) + math.pow(self.verticies[curr].Y - self.verticies[goal.index].Y,2))
			print "iter=%d, frontier=%d, popped=%d (%d,%d), depth=%d, dist2goal=%.1f"%(i,len(queue),curr, self.verticies[curr].X, self.verticies[curr].Y, self.nodes[curr].depth, dist2goal)

		for x in self.nodes[curr].successors():
			if self.nodes[x].depth == -1 :     #if index not visited
				self.nodes[x].parent = self.nodes[curr]
				self.nodes[x].depth =  self.nodes[curr].depth + 1 
				self.nodes[x].heur = math.sqrt(math.pow(self.verticies[x].X - self.verticies[goal.index].X ,2) + math.pow(self.verticies[x].Y - self.verticies[goal.index].Y,2)) + math.sqrt(math.pow(self.verticies[x].X - self.verticies[initial_state.index].X ,2) + math.pow(self.verticies[x].Y - self.verticies[initial_state.index].Y,2))
				queue[x] = self.nodes[x].heur
				self.nodes[x].tracebacks = self.nodes[curr].tracebacks + [x]
				v += 1
				if self.debug==1 :
					print "pushed %d (%d,%d)"%(x, self.verticies[x].X, self.verticies[x].Y)
		if len(queue) > max:
			max = len(queue)
