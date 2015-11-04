#!/usr/bin/python
import argparse
import sys
from state import Node
from state import Vertex
from graph import Graph
from state import  GlobalVariable
from graph import  InitialState
from report import Report
import time
if __name__ == "__main__":



    parser = argparse.ArgumentParser(description='Solve Block problem')
    parser.add_argument('--d', dest='debug', action='store_true', help="THIS IS debu FLAG")
    parser.set_defaults(debug = False)
    parser.add_argument('--p', dest='prun', action='store_true', help="THIS IS Pruning FLAG")
    parser.set_defaults(prun = False)
    parser.add_argument('--g', dest='greedy', action='store_true', help="THIS IS Greedy FLAG")
    parser.set_defaults(greedy = False)

    parser.add_argument("other_args", nargs = "*", default = [3,5,"All"])
    args = parser.parse_args()
    other_args = args.other_args
    if len(other_args) < 2:
        print "Arguments are in wrong format"
    	sys.exit()
    for i in range(0,2):
        try:
            other_args[i] = int(other_args[i])
    	except:
            print "Arguments are in wrong format"
            sys.exit()

    if args.prun :
        GlobalVariable.prun = True

    if args.greedy:
        GlobalVariable.isgreedy = True

    if args.debug:
        GlobalVariable.debug = True
    iscustom = True
    isdefault = True
    if len(other_args) == 3 :
        if other_args[2] == "custom":
            iscustom = True
            isdefault = False
        elif other_args[2] == "default" :
            isdefault = True
            iscustom = False


    stacks = args.other_args[0]
    blocks = args.other_args[1]
    #initialstate = [['H', 'D', 'E'],['G', 'I', 'F'],['A', 'B', 'C']]

    obj = InitialState(stacks, blocks)
    initialstate = obj.create_initialstate()

    initialvertex = Vertex(initialstate)

    print "Initial State:"
    initialvertex.display()

    if iscustom:
        #Solving problem with Custom Heuristic
        initialnode_custom = Node(initialvertex, None, 1)
        game_custom = Graph(initialnode_custom)
        print "Solving by {0} . . . . . . . . ".format("Custom Heuristic")
        start = time.time()
        iteration_custom, pathlength_custom,heapsize_custom,visitedstate_custom, path_custom = game_custom.solve()
        time_custom = time.time() - start
        print "Time taken: {0} seconds".format(time_custom)

    if isdefault:
        # Solving problem with Default Heuristic
        initialnode_default = Node(initialvertex, None, 0)
        game_default = Graph(initialnode_default)
        print "Solving by  {0} . . . . . . . . ".format("Block in place(default) Heuristic")
        start = time.time()
        iteration_default, pathlength_default,heapsize_default,visitedstate_default, path_default = game_default.solve()
        time_default = time.time() - start
        print "Time taken: {0} seconds".format(time_default)







    #Generate Report
    if iscustom and isdefault:
        report = Report()
        report.iterations(str(iteration_default), str(-1), str(iteration_custom))
        report.pathlength(str(pathlength_default), str(-1),str(pathlength_custom))
        report.queuesize(str(heapsize_default), str(-1),str(heapsize_custom))
        report.statesvisited(str(visitedstate_default), str(-1),str(visitedstate_custom))
        report.displaystate(initialstate)
        report.displayfilepath()
        report.saveandclose()

    #Saving solution files
    if isdefault:
        k = 1
        inplace_file = open("inplaceblocks_solution.txt","w")
        inplace_file.write("              Solution: In Place Blocks Heuristic \n\n")
        for x in path_default:
            inplace_file.write("________________STATE {0}______________________\n\n".format(str(k)))
            for stack in x.vertex.stacks:
                inplace_file.write("{0}\n".format(str(stack)))
            k += 1
            inplace_file.write("\n")

    if iscustom:
        k = 1
        inplace_file = open("customheuristic_solution.txt","w")
        inplace_file.write("              Solution: Custom Heuristic \n\n")
        for x in path_custom:
            inplace_file.write("________________STATE {0}______________________\n\n".format(str(k)))
            for stack in x.vertex.stacks:
                inplace_file.write("{0}\n".format(str(stack)))
            k += 1
            inplace_file.write("\n")

