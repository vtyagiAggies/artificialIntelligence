#!/usr/bin/python
import sys
class Clause:
    def __init__(self,id, value, parentOne = -1, parentTwo = -1):
        self.ID = id
        self.value = value
        self.value.sort()
        self.parentOne = parentOne
        self.parentTwo = parentTwo
        self.len = len(value)           #heuristic whihc is required to maintain values in prioriy queue

class Clauses:
    def __init__(self, strPathToFile):
        self.strPathToFile = strPathToFile
        self.clauses = {}
        self.candidateDict = {}             #To prevent duplicate clauses
        self.lastClauseID = -1

    def addClause(self, value, pair = [-1,-1]):
        value = list(set(value))
        hashOfClauseValue = ''.join(value)
        
        if not self.candidateDict.has_key(hashOfClauseValue):
            self.lastClauseID += 1
            newClause = Clause(self.lastClauseID, value, pair[0], pair[1])
            self.clauses[self.lastClauseID] = newClause
            self.candidateDict[hashOfClauseValue] = True

            if Global.debug:
                strClause = self.toString(value)
                if pair == [-1,-1]:
                    print "{0}: {1}".format(self.lastClauseID, strClause)
                elif strClause != "":
                    print "{0}: {1} generated from {2} and {3}".format(self.lastClauseID, strClause, pair[0], pair[1])


    def toString(self, clause):
        flag = False
        strClause= ""
        for x in clause:
            if flag :
                strClause += " v "
            strClause += x
            flag = True
        return strClause

    def parse(self):
        try:
            objClausesFile = open(self.strPathToFile)
        except:
            print "File doesn't exist at path: {0}".format(self.strPathToFile)
            sys.exit()
        lines = [line.strip().split(' ')  for line in objClausesFile.readlines() if len(line.strip()) > 0 and line[0] != "#"]

        for i in range(len(lines)):
            self.addClause(lines[i])


    def heuristic(self,pair):
        return  self.clauses[pair[0]].len + self.clauses[pair[1]].len

    def isResovable(self,i,j):
        clauseOne = self.clauses[i].value
        clauseTwo = self.clauses[j].value
        negatableComponent = []
        for x in clauseOne:
            for y in clauseTwo:
                if x == ("-"+y) or "-"+x == y:
                    negatableComponent.append(x)
        if negatableComponent == []:
            return  False
        else:
            return  True

    def resolvePair1(self, pair):                #Return empty list if two clause cannot be resolved
        clauseOne = self.clauses[pair[0]].value
        clauseTwo = self.clauses[pair[1]].value
        negatableComponent = []
        result = []

        for x in clauseOne:
            for y in clauseTwo:
                if x == ("-"+y) or "-"+x == y:
                    negatableComponent.append(x)

        newClauseValue = []
        for var in negatableComponent:
            flag = True
            for x in clauseOne:
                if flag and (x == var or "-"+x == var or x == "-" + var):
                    flag = False
                    continue
                else:
                    newClauseValue.append(x)
            flag = True
            for y in clauseTwo:
                if flag and (y == var or "-" + y == var or y == "-" + var):
                    flag = False
                    continue
                else:
                    newClauseValue.append(y)
            newClauseValue.sort()
            result.append(newClauseValue)
            newClauseValue = []

        return  result

    def resolvePair(self, pair):                #Return empty list if two clause cannot be resolved
        clauseOne = self.clauses[pair[0]].value
        clauseTwo = self.clauses[pair[1]].value
        negatableComponent = {}
        result = []
        for x in clauseOne:
            if x[0] == "-":
                negatableComponent[x] = True
        for y in clauseTwo:
            if y[0] == "-":
                negatableComponent[y] = True
        for key in negatableComponent.keys():
            newClauseValue  = []
            oppKey = key[1:]
            combined = clauseOne + clauseTwo
            flag = False
            for x in combined:
                if x == oppKey:
                    flag = True
                    break
            if flag:
                for x in combined:
                    if x == key:
                        key  = []
                        continue
                    if x == oppKey:
                        oppKey = []
                        continue

                    newClauseValue.append(x)
                newClauseValue.sort()
                result.append(newClauseValue)
        return result



class Global:
    debug = False
