#!/usr/bin/python
import  copy
import  sys

class Jobs:
    def __init__(self):
        self.variables = {"Roberta": 0, "Thelma" : 0, "Steve" : 0, "Pete" : 0}
        self.domains = self.getdomains()
        self.reduceddomains = copy.deepcopy(self.domains)


    def getdomains(self):
        domain = {"Roberta":[],"Thelma":[],"Steve":[],"Pete":[]}
        jobs = ["chef", "guard", "nurse", "clerk", "police officer","teacher", "actor", "boxer"]
        for key in domain:
            for x in jobs:
                for y in jobs:
                    if x != y:
                        domain[key].append([x,y])
        return domain

    def iscomplete(self, assignment):
        for variable in self.variables:
            if not assignment.has_key(variable):
                return False
        return True

    def get_unassigned_variable(self, assignment):
        # check for Roberta
        for variable in self.variables:
            if not assignment.has_key(variable):
                return variable
        return "all assigned"

    def get_unassigned_variable_with_minimum_value(self, assignment):
        # check for Roberta
        min = sys.maxint
        result = ""
        for variable in self.variables:
            if not assignment.has_key(variable):
                if len(self.reduceddomains[variable]) < min:
                    min = len(self.reduceddomains[variable])
                    result = variable
        return result

    def reducedomain_forvalue(self, svalue, variable, value):
        if (svalue[0] in value or svalue[1] in value):
            self.reduceddomains[variable].remove(value)
            return
        if ("boxer" in value or "police officer" in value or "chef" in value) and variable == "Roberta":
            self.reduceddomains[variable].remove(value)
            return
        if ("nurse" in value or "clerk" in value or "actor" in value) and (variable == "Roberta" or variable == "Thelma"):
            self.reduceddomains[variable].remove(value)
            return
        if "chef" in value and (variable == "Steve" or variable == "Pete"):
            self.reduceddomains[variable].remove(value)
            return
        if ("nurse" in value or "police officer" in value or "teacher" in value) and (variable == "Pete"):
            self.reduceddomains[variable].remove(value)
            return
        if "chef" in value  and "police officer" in value:
            self.reduceddomains[variable].remove(value)
            return

    def resetreduceddomains(self):
        self.reduceddomains =  copy.deepcopy(self.domains)

    def consistencycheck(self, assignment):
            return self.consistency_jobs(assignment)


    def consistency_jobs(self, assignment):
        alldiff = {}
        #consistency check for Roberta
        if assignment.has_key("Roberta"):
            roberta_values = assignment["Roberta"]
            for value in roberta_values:
                if alldiff.has_key(value):
                    return False
                else:
                    alldiff[value] = True
                if value in ["chef","nurse","clerk","actor","boxer","police officer"]:
                    return False

        #consistency check for Thelma
        if assignment.has_key("Thelma"):
            therma_values = assignment["Thelma"]
            if "chef" in therma_values and "police officer" in therma_values:
                return False
            for value in therma_values:
                if alldiff.has_key(value):
                    return False
                else:
                    alldiff[value] = True
                if value in ["nurse","clerk","actor"]:
                    return False

        #consistency check for Steve
        if assignment.has_key("Steve"):
            steve_values = assignment["Steve"]
            if "chef" in steve_values and "police officer" in steve_values:
                return False
            for value in steve_values:
                if alldiff.has_key(value):
                    return False
                else:
                    alldiff[value] = True
                if value in ["chef"]:
                    return False

        #consistency check for Pete
        if assignment.has_key("Pete"):
            pete_values = assignment["Pete"]
            if "chef" in pete_values and "police officer" in pete_values:
                return False
            for value in pete_values:
                if alldiff.has_key(value):
                    return False
                else:
                    alldiff[value] = True
                if value in ["chef","nurse","police officer","teacher"]:
                    return False


        return True             #if satisfies all constraints

