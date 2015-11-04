#!/usr/bin/python
import sys
import random
from state import Node
from state import Vertex, GlobalVariable
from priorityqueue import Priorityqueue


class Graph:
    def __init__(self, initial):
        self.initial = initial
        self.visited = {}  # Hash to record visited nodes
        self.visited[initial.vertex.gethash()] = True
        self.defaultpathlength = 100000

    def solve(self):
        queue = Priorityqueue([self.initial])
        i = 0
        maxheapsize = 1
        h = 1
        path = []
        found = False
        a,b,c,d  = -1,-1,-1,-1
        while len(queue.heap) > 1:
            if len(self.visited) > 1000000:
                print "No. of Iterations crossed 10,00,000. Exiting.."
                sys.exit()
            curr = queue.popmax()
            if GlobalVariable.debug:
                print "iter = {0}, queue = {1}, heur = {2}, depth = {3}".format(i,len(queue.heap), curr.heur, curr.depth)
            i += 1
            h -= 1

            if curr.isgoalstate():
                path = curr.tracebacks()
                path.append(curr)
                a,b,c,d = i, len(path), maxheapsize, len(self.visited)
                found = True
                if GlobalVariable.debug:
                    k = 1
                    print "              Solution: In Place Blocks Heuristic "
                    for x in path:
                        print "________________STATE {0}______________________".format(str(k))
                        for stack in x.vertex.stacks:
                            print "{0}".format(str(stack))
                        k += 1
                print "Iterations: %d" % (i)
                print "Path Length: %d" % len(path)
                print "Maximum queue size: %d" % (maxheapsize)
                print "Number of states visited: %d" % (len(self.visited))
                return i, len(path), maxheapsize, len(self.visited), path
            for x in curr.successors():
                if not self.visited.has_key(x.vertex.gethash()):
                    self.visited[x.vertex.gethash()] = x.depth
                    queue.insert(x)
                    h += 1
                elif self.visited[x.vertex.gethash()] > x.depth:
                    del self.visited[x.vertex.gethash()]
                    self.visited[x.vertex.gethash()] = x.depth
                    queue.insert(x)
            if h > maxheapsize:
               maxheapsize = h
            #sprint i, maxheapsize, len(self.visited)
            if GlobalVariable.prun:
                if len(queue.heap) > 1000:
                    del queue.heap[100:]


        print "Iterations: %d" % (a+1)
        print "Path Length: %d" % b
        print "Maximum queue size: %d" % c
        print "Number of states visited: %d" % d
        return a, b, c, d, path


class InitialState:
    def __init__(self, m, blocks):
        self.m = m
        self.blocks = blocks

    def create_initialstate(self):
		initialstate = []
		checked = {}
		for i in range(self.m):
			initialstate.append([])


		for i in range(self.blocks):
			var = random.randint(1,self.blocks)
			while checked.has_key(var):
				var = random.randint(1,self.blocks)
			checked[var] = True
			pos = random.randint(0,self.m-1)
			initialstate[pos] += [str(unichr(var+64))]
		return initialstate

