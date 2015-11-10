#!/usr/bin/python
import copy
class Solver:

    """Sovling puzzle by backtracking"""
    def solve_by_backtracking(self, csp):
        return self.backtrack({}, csp)

    def backtrack(self, assignment, csp):
        if csp.iscomplete(assignment):
            return assignment

        result = {}
        var = csp.get_unassigned_variable(assignment)
        for value in csp.domains[var]:
            Global.counter += 1
            assignment[var] = value
            if csp.consistencycheck(assignment) == True:
                result = self.backtrack(assignment,csp)
                if result != {} :
                    return result
            del assignment[var]
        return result

    #Solving using MRV (Minimum remaining values
    def solve_by_mrv(self, csp):
        return self.mrv({}, csp)

    def mrv(self, assignment, csp):
        if csp.iscomplete(assignment):
            return assignment

        result = {}
        var = csp.get_unassigned_variable_with_minimum_value(assignment)
        for value in csp.reduceddomains[var]:
            Global.counter += 1
            assignment[var] = value
            if csp.consistencycheck(assignment) == True:
                self.reducedomain(var,value, assignment, csp)
                result = self.mrv(assignment,csp)
                if result != {} :
                    return result
                self.resetdomainforvariable( var,assignment, csp)
            del assignment[var]
        return result

    #reducing domain values and reseting them
    def resetdomainforvariable(self, var, assignment, csp):
        for variable in csp.variables:
            if not assignment.has_key(variable) and variable != var:
                csp.reduceddomains[variable] = copy.deepcopy(csp.domains[variable])

    def reducedomain(self, var, svalue, assignment, csp):
        for variable in csp.variables:
            if not assignment.has_key(variable)  and var != variable:
                for value in csp.reduceddomains[variable]:
                    csp.reducedomain_forvalue(svalue, variable, value)


class Global:
    counter = 0
    result = []
