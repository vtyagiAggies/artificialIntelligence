#!/usr/bin/python
from clauses import Clauses
from priorityqueue import Priorityqueue
from clauses import Global
class Solver:
    def __init__(self, strPathToInputFile):
        self.strPathToinputFile = strPathToInputFile
        self.clauses = Clauses(strPathToInputFile)
        self.clauses.parse()
        self.candidates = Priorityqueue(self.clauses)
        self.heapDict = {}



    def getInitialCandidates(self):
        for i in range(self.clauses.lastClauseID + 1):
            for j in range(i+1,self.clauses.lastClauseID + 1):
                if i != j and self.clauses.isResovable(i,j):
                    self.candidates.insert([i,j])



    def solveByResolution(self):
        self.getInitialCandidates()
        iter = 1
        maxquesize = 0
        while (len(self.candidates.heap) > 1):
            if len(self.candidates.heap)-1 > maxquesize:
                maxquesize = len(self.candidates.heap) -1
            pairToBeResolved = self.candidates.popmax()
            listOfResolvent = self.clauses.resolvePair(pairToBeResolved)
            if Global.debug:
                print "Iteration {0}, queue size {1}, resolution on {2} and {3}".format(iter, len(self.candidates.heap), pairToBeResolved[0], pairToBeResolved[1])
                print "Resolving {0} and {1}".format(self.clauses.toString(self.clauses.clauses[pairToBeResolved[0]].value), self.clauses.toString(self.clauses.clauses[pairToBeResolved[1]].value))
            for resolvent in listOfResolvent:
                self.clauses.addClause(resolvent,pairToBeResolved)   #Add clause takes care of duplicate clauses
                if len(resolvent) == 0:
                    print "Maximum Queue size: {0}".format(maxquesize)
                    return True
            for i in range(self.clauses.lastClauseID):
                if self.clauses.isResovable(i, self.clauses.lastClauseID):
                    listOfResolvent = self.clauses.resolvePair([i,self.clauses.lastClauseID])
                    for resolvent in listOfResolvent:
                        key = str(i) + "," + str(self.clauses.lastClauseID)
                        if not (self.clauses.candidateDict.has_key(''.join(resolvent)) and self.heapDict.has_key(key)):
                            if not self.heapDict.has_key(key):
                                self.candidates.insert([i, self.clauses.lastClauseID])
                                self.heapDict[key] = True     #Todo
            iter += 1
        print "Maximum queue size {0}".format(maxquesize)
        return False


    def printResult(self,id):
        self.printPattern(id,0)

    def printPattern(self,id,depth):
        clause = self.clauses.clauses[id].value
        strClause = self.clauses.toString(clause)
        parent= ""
        if self.clauses.clauses[id].parentOne == -1:
            parent = "[input]"
        else:
            parent = "{0}".format([self.clauses.clauses[id].parentOne, self.clauses.clauses[id].parentTwo])
        if strClause == "":
            strClause = "[]"
        for i in range(depth):
            print " ",
        print "{0}: {1} {2}".format(id, strClause, parent)
        if self.clauses.clauses[id].parentOne == -1:
            return
        self.printPattern(self.clauses.clauses[id].parentOne, depth + 1)
        self.printPattern(self.clauses.clauses[id].parentTwo, depth + 1)
        return







