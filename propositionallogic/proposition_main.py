#!/usr/bin/python
import sys
import argparse
from solver import Solver
from clauses import Global



if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Find steps for propositional logic problem")
    parser.add_argument('--debug', dest='debug', action='store_true', help="THIS IS DEBUG FLAG")
    parser.set_defaults(debug = False)
    parser.add_argument("other_args", nargs = "*", default = ["input.txt"])
    args = parser.parse_args()
    other_args = args.other_args
    if len(other_args) != 1 or not isinstance(other_args[0], str):
        print "Arguments are in wrong format"
        sys.exit()
    if args.debug:
        Global.debug = True

    strPathToInputFile = other_args[0]

    objSolver = Solver(strPathToInputFile)

    if objSolver.solveByResolution():
        print "success! empty clause found"
        objSolver.printResult(objSolver.clauses.lastClauseID)
    else:
        print "Failure returend!!"




       



