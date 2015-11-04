#!/usr/bin/python
import sys

class Priorityqueue:                        #Modified Priority Queue to sort nodes on basis of their hueristic value
    def __init__(self, array = []):
        self.heap  = [-1]
        self.heapify(array)                 #heap as a one-dimensional array will represent binary tree, heap[0] stores nothing; to access children for k node 2*k and 2*k + 1; to access parent of k node 2*k

    def heapify(self, array):
        if array != []:
            for x in array:
                self.insert((x))
           

    def insert(self, x):
        self.heap.append(x)
        k = len(self.heap)-1
        while(k > 1 and self.heap[k/2].heur < self.heap[k].heur):         #swim effect in heap moving greater element upwards
            self.heap[k/2], self.heap[k] = self.heap[k], self.heap[k/2]
            k = k/2
        

    def getmax(self):
        return self.heap[1] #maximum element will be at root

    def popmax(self):
        if len(self.heap) < 2:
            return -1
        result = self.heap[1]
        h = self.heap
        l = len(self.heap)
        self.heap[1] = self.heap[l-1]
        del self.heap[l-1:]
        l -= 1
        k = 1
        while (2*k < l):                #sink effec taking minimum element down the tree
            if (2*k + 1) < l and (h[k].heur < h[2*k].heur or h[k].heur < h[2*k+1].heur) :
                if h[2*k].heur > h[2*k+1].heur:
                    self.heap[k], self.heap[2*k] = self.heap[2*k], self.heap[k]
                    k = 2*k
                else:
                     self.heap[k], self.heap[2*k+1] = self.heap[2*k+1], self.heap[k]
                     k = 2*k+1
            elif ((2*k) < l and self.heap[k].heur < self.heap[2*k].heur):
                self.heap[k], self.heap[2*k] = self.heap[2*k], self.heap[k]
                k = 2*k
            else:
                break
        return result
