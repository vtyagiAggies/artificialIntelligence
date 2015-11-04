#!/usr/bin/python

class Report:
    def __init__(self, filename="report.html"):
        self.obj = open(filename, "w")
        self.obj.write(
            "<html><head><Title>AI Homework 2 Report</Title><style>table, th, td {border: 1px solid black;border-collapse: collapse;}th, td {padding: 5px;text-align: center;}</style></head> <body><h1 align=\"center\"><u>Analysis of different heuristics for Block game!!</u></h1><br><br><br><br><br><br><table border=\"1\" align =\"center\">")
        self.obj.write(
            "<tr><th>Properties</th><th>Block in place Heuristic</th><th>Customized Heuristic</th></tr>")

    def iterations(self, a=-1, b=-1, c=-1):
        self.obj.write(
            "<tr><td><b>Iterations</b></td><td>{0}</td><td>{1}</td></tr>".format(str(a), str(c)))

    def pathlength(self, a=-1, b=-1, c=-1):
        self.obj.write(
            "<tr><td><b>Path Length</b></td><td>{0}</td><td>{1}</td></tr>".format(str(a), str(c)))

    def queuesize(self, a=-1, b=-1, c=-1):
        self.obj.write(
            "<tr><td><b>Maximum Queue Length</b></td><td>{0}</td><td>{1}</td></tr>".format(str(a), str(c)))

    def statesvisited(self, a=-1, b=-1, c=-1):
        self.obj.write(
            "<tr><td><b>Number of states visited</b></td><td>{0}</td><td>{1}</td></tr>".format(str(a), str(c)))
        self.obj.write("</table>")

    def saveandclose(self):
        self.obj.write("</body></html>")
        self.obj.close()

    def displaystate(self,array):
        self.obj.write("\n<br/><br/><br/><br/><br/><div ><h1 ><u>Initial state</u></h1><h2 align =\"left\">")
        k = 1
        for stack in array:
            self.obj.write("Stack {0} : {1} <br>".format(k, str(stack)))
            k += 1

        self.obj.write("</h2></div>")

    def displayfilepath(self):
        self.obj.write("\n<br/><br/><br/><br/><br/><div ><h1 ><u>Path to goal state</u></h1><h2 align =\"left\">")
        self.obj.write("<ul><li><a href=\"inplaceblocks_solution.txt\">In Place Blocks Heuristic</a></li> <li><a href=\"customheuristic_solution.txt\">Custom Heuristic</a></li></ul>")

        self.obj.write("</h2></div>")