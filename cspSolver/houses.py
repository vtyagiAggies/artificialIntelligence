#!/usr/bin/python
import  sys
import copy
class Houses:
    def __init__(self):
        self.variables = [1, 2, 3, 4, 5]
        self.domains = self.getdomains()
        self.reduceddomains = copy.deepcopy(self.domains)


    def getdomains(self):
        domain = {1:[],2:[],3:[],4:[],5:[]}
        country = ["Norwegian", "Spaniard", "English", "Ukranian", "Japanese"]
        eats = ["kit kats", "hershey bars",  "smarties", "snickers", "milky way"]
        drinks = ["water","orange juice", "tea", "coffee", "milk"]
        colors = ["yellow", "red", "green", "ivory",  "blue"]
        animals = [ "fox","dog", "snails", "horse", "zebra"]
        for i in range(1,6):
            for j in range(5):
                for k in range(5):
                    for l in range(5):
                        for m in range(5):
                            for n in range(5):
                                domain[i].append({"country": country[j],"eat" :eats[k], "drink" :drinks[l],"color" :colors[m], "animal" : animals[n]})
        return domain

    def get_unassigned_variable_with_minimum_value(self, assignment):
        min = sys.maxint
        result = 0
        for i in range(1, 6):
            if not assignment.has_key(i):
                if len(self.reduceddomains[i]) < min:
                    min =  len(self.reduceddomains[i])
                    result = i
        return result

    def get_unassigned_variable(self, assignment):
        for i in range(1, 6):
            if not assignment.has_key(i):
                return i
        return 0

    def reducedomain_forvalue(self,svalue, variable, value):

        if (svalue['country'] == value['country'] or svalue['eat'] == value['eat'] or svalue['drink'] == value['drink'] or svalue['color'] == value['color'] or svalue['animal'] == value['animal']):
            self.reduceddomains[variable].remove(value)
            return
        if value['country'] == "English" and value['color'] != "red":
            self.reduceddomains[variable].remove(value)
            return
        if value['country'] == "Spaniard" and value['animal'] != "dog":
            self.reduceddomains[variable].remove(value)
            return
        if value['country'] == "Norwegian" and variable != 1:
            self.reduceddomains[variable].remove(value)
            return
        if value['color'] == "yellow" and value['eat'] != "kit kats":
            self.reduceddomains[variable].remove(value)
            return
        if value['eat'] == "snickers" and value['drink'] != "orange juice":
            self.reduceddomains[variable].remove(value)
            return
        if value['animal'] == "snails" and value['eat'] != "smarties":
            self.reduceddomains[variable].remove(value)
            return
        if value['country'] == "Ukranian" and value['drink'] != "tea":
            self.reduceddomains[variable].remove(value)
            return
        if value['country'] == "Japanese" and value['eat'] != "milky way":
            self.reduceddomains[variable].remove(value)
            return
        if value['color'] == "green" and value['drink'] != "coffee":
            self.reduceddomains[variable].remove(value)
            return

    def iscomplete(self,assignment):
        for i in range(1,6):
            if not assignment.has_key(i):
                return False
        return True

    def consistencycheck(self, assignment):
            return self.consistency_houses(assignment)

    def consistency_houses(self, assignment):
        alldiffc = {}
        alldiffe = {}
        alldiffd = {}
        alldiffa = {}
        alldiffco = {}
        for i in range(1,6):
            if assignment.has_key(i):
                housevalues = assignment[i]
                #Constraint all having differnet values
                if alldiffc.has_key(housevalues["country"]):
                    return False
                else:
                    alldiffc[housevalues["country"]] = True
                if alldiffe.has_key(housevalues["eat"]):
                    return False
                else:
                    alldiffe[housevalues["eat"]] = True
                if alldiffd.has_key(housevalues["drink"]):
                    return False
                else:
                    alldiffd[housevalues["drink"]] = True
                if alldiffa.has_key(housevalues["animal"]):
                    return False
                else:
                    alldiffa[housevalues["animal"]] = True
                if alldiffco.has_key(housevalues["color"]):
                    return False
                else:
                    alldiffco[housevalues["color"]] = True

                if ((housevalues["country"] == "English")^(housevalues["color"] == "red")):                                                                         #constraint 1
                    return False
                if ((housevalues["country"] == "Spaniard")^(housevalues["animal"] == "dog")):                                                                       #constraint 2
                    return False
                if ((housevalues["country"] == "Norwegian") and (i != 1)):                                                                                          #constraint 3
                    return False
                if ((housevalues["color"] == "green") and i > 1 and assignment.has_key(i-1) and (assignment[i-1]["color"] != "ivory")) or ((housevalues["color"] == "green") and i == 1):       #constraint 4
                    return False
                if ((i == 1 and housevalues["eat"] == "hershey bars" and assignment.has_key(2) and assignment[2]["animal"] != "fox")  or   (i == 6 and housevalues["eat"] == "hershey bars" and assignment.has_key(5) and assignment[5]["animal"] != "fox")
                    or ((i > 1 and i < 6) and housevalues["eat"] == "hershey bars"  and assignment.has_key(i-1) and assignment.has_key(i+1) and assignment[i-1]["animal"] != "fox" and assignment[i+1]["animal"] != "fox" )):
                    return False                                                                                                                                    #constraint 5
                if ((housevalues["eat"] == "kit kats")^(housevalues["color"] == "yellow")):                                                                         #constraint 6
                    return False
                if ((i == 1 and housevalues["country"] == "Norwegian" and assignment.has_key(2) and assignment[2]["color"] != "blue")  or   (i == 6 and housevalues["country"] == "Norwegian" and assignment.has_key(5) and assignment[5]["color"] != "blue")
                    or ((i > 1 and i < 6) and housevalues["country"] == "Norwegian"  and assignment.has_key(i-1) and assignment.has_key(i+1) and assignment[i-1]["color"] != "blue" and assignment[i+1]["color"] != "blue")):
                    return False                                                                                                                                    #constraint 7
                if ((housevalues["eat"] == "smarties")^(housevalues["animal"] == "snails")):                                                                        #constraint 8
                    return False
                if ((housevalues["eat"] == "snickers")^(housevalues["drink"] == "orange juice")):                                                                   #constraint 9
                    return False
                if ((housevalues["country"] == "Ukranian")^(housevalues["drink"] == "tea")):                                                                        #constraint 10
                    return False
                if ((housevalues["country"] == "Japanese")^(housevalues["eat"] == "milky way")):                                                                    #constraint 11
                    return False
                if ((i == 1 and housevalues["eat"] == "kit kats" and assignment.has_key(2) and assignment[2]["animal"] != "horse")  or   (i == 6 and housevalues["eat"] == "kit kats" and assignment.has_key(5) and assignment[5]["animal"] != "horse")
                    or ((i > 1 and i < 6) and housevalues["eat"] == "kit kats"  and assignment.has_key(i-1) and assignment.has_key(i+1)  and assignment[i-1]["animal"] != "horse" and assignment[i+1]["animal"] != "horse" )):
                    return False                                                                                                                                    #constraint 12
                if ((housevalues["drink"] == "coffee")^(housevalues["color"] == "green")):                                                                         #constraint 13
                    return False
                if ((housevalues["drink"] == "milk")and (i != 3)):                                                                                                #constraint 14
                    return False
                #constraint 15 & 16 automatically satisfy

        return True

