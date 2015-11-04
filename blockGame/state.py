#!/usr/bin/python
import copy

#Class for Vertex
class Vertex:
    def __init__(self, stacks):
        self.stacks = stacks          #Type: List[List[char]]
    
    def gethash(self):
	    k = 1
	    result = ""
	    for stack in self.stacks:
                result += str(k)
                result += ''.join(stack)
                k += 1
	    return result

    def display(self):
        print "____________________________________"
        for stack in self.stacks:
            print stack
        print "____________________________________"
        
        
class Node:
    def __init__(self, vertex, parent = None, heurtype = 0, depth = 0) :
        self.vertex = vertex                #Type: Vertex
        self.parent = parent
        self.depth = depth
        self.heurtype = heurtype
        if self.heurtype == 0:
            self.heur = self.defaultheuristic()
        elif self.heurtype == 1:
            self.heur = self.customheuristic()
        self.successor = []
        self.traceback = []

    def successors(self):
        if self.successor == [] :
            for i in range(len(self.vertex.stacks)):                #stores all possible next states in successor
               #print newstacks
               for j in range(len(self.vertex.stacks)) :
                   newstacks = copy.deepcopy(self.vertex.stacks)
                   if len(newstacks[i]) > 0:
                       temp = newstacks[i][len(newstacks[i]) - 1]
                       del newstacks[i][len(newstacks[i])-1:]
                       if(i==j) :
                           continue
                       newstacks[j].append(temp)
                       nextnode = Node(Vertex(newstacks),self, self.heurtype, self.depth + 1)
                       for x in self.traceback:
                            nextnode.traceback.append(x)
                       nextnode.traceback.append(self)   #adding parent
                       self.successor.append(nextnode)
        return self.successor
    
    def tracebacks(self):
        return self.traceback

    def setheuristictype(self, type):
        self.heurtype = type
                        
    def defaultheuristic(self):
        firststack = self.vertex.stacks[0]
        #print firststack
        score = 0.0
        for x in firststack:
            #print x, ord(x), score
            if ord(x) == (65 +int(score)):
                score += 1
            else: 
                break
        if not GlobalVariable.isgreedy :
            score -= self.depth
        return score

    def customheuristic(self):
        firststack = self.vertex.stacks[0]
        score = 0.0
        if not GlobalVariable.isgreedy:
            score -= 5*self.depth
        k = 0
        extrapoint = True
        for x in firststack:
            if ord(x) == (65 + k):
                score += 10
            else:
                extrapoint = False              #last element is not in sequence
                score -= 5
                break
            k += 1

        if extrapoint and len(firststack) > 0:                         #If top element of any other stack is next to top of perfect first stack
            for i in range(1,len(self.vertex.stacks)):
                if len(self.vertex.stacks[i]) > 0 and (self.vertex.stacks[i][len(self.vertex.stacks[i]) - 1]) == ord(firststack[k-1]) + 1:
                    score += 5
                    break

        for i in range(1,len(self.vertex.stacks)):
            stack = self.vertex.stacks[i]
            for i in range(len(stack) - 2, -1, -1):
                if ord(stack[i]) == ord(stack[i+1]) + 1:
                    score += 1
                else :
                    break
                '''if len(firststack) > 0 and extrapoint and ord(stack[i]) == ord(firststack[k-1]) + 1 :
                    score -= (len(stack) - i - 1) * 10'''
        #print score
        return  score

    
    def isgoalstate(self):
        firststack = self.vertex.stacks[0]
        k = 0
        for x in firststack:
            if ord(x)  == (65 + k):
                k += 1
            else:
                return False
        for i in range(1, len(self.vertex.stacks)):
            if len(self.vertex.stacks[i]) > 0:
               return False
        return True

class GlobalVariable:
    prun = False
    isgreedy = False
    debug = False