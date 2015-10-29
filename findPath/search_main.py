#!/usr/bin/python
import sys
import argparse
from Graph import Graph	
from Nodes import Node
from Nodes import GlobalVariable			

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Find path from given source to destination using passed search algorithm(BFS, DFS, GBFS, ASTAR in given graph.')
	parser.add_argument('--debug', dest='debug', action='store_true', help="THIS IS DEBUG FLAG")
	parser.set_defaults(debug = False)
	parser.add_argument("other_args", nargs = "*", default = ["ATM.graph","BFS", 1, 20, 20, 1])
	args = parser.parse_args()
	other_args = args.other_args
	if len(other_args) != 6 or not isinstance(other_args[0], str) or not isinstance(other_args[1], str):
    		print "Arguments are in wrong format"
    		sys.exit()
	for i in range(2,6):
    		try:
        		other_args[i] = int(other_args[i])
    		except:
        		print "Arguments are in wrong format"
        		sys.exit()
	if args.debug:
    		GlobalVariable.debug = 1
	filepath = args.other_args[0]
	search_algo = args.other_args[1]
	source_x = int(args.other_args[2])
	source_y =int(args.other_args[3])
	destination_x =int(args.other_args[4])
	destination_y = int(args.other_args[5])
	if source_x  not in range(1,21) or destination_x not in range(1,21) or source_y not in range(1,21) or destination_y  not in range(1,21) :
		print "Coordinates are out of range"
		sys.exit()
	if search_algo not in ["BFS", "DFS", "GBFS", "ASTAR"] :
		print "%s: It is not desired search algorithm please select from (BFS, DFS, GBFS, ASTAR)"%(search_algo)
		sys.exit()

    	#Intializing graph
	foundX = False
	foundY = False
	graph = Graph(filepath)
	for vertex in graph.verticies:
		if(vertex.X == source_x and vertex.Y == source_y):
			initial_state = Node(vertex.ID)
			foundX = True
		if(vertex.X == destination_x and vertex.Y == destination_y):
			goal = Node(vertex.ID)
			foundY = True
	if not foundX :
		print "Initial state is unreachable"
		sys.exit()
	if not foundY :
		print "Destination state is unreachable"
		sys.exit()
 
	#Calling search algorithm according to user input
	if(search_algo == "BFS"):
		traceback, vertices_visited, iterations, max  = graph.BFS_Search(initial_state, goal)
	elif(search_algo == "DFS"):
		traceback, vertices_visited, iterations, max  = graph.DFS_Search(initial_state, goal)
	elif search_algo == "GBFS":
		traceback, vertices_visited, iterations, max  = graph.GBFS_Search(initial_state, goal)
	elif search_algo == "ASTAR":
		traceback, vertices_visited, iterations, max  = graph.ASTAR_Search(initial_state, goal)


	#Printing 
	if GlobalVariable.debug :
		print "======================================================================="		
	print "Solution path:"
	for x in traceback:
		print "%d %d"%(graph.verticies[x].X, graph.verticies[x].Y)
	print "Search algorithm  = ", search_algo
	print "Total iterations  = %d"%(iterations)
	print "Max frontier size = %d"%(max)
	print "Vertices visited  = %d/275"%(vertices_visited)
	print "Path length       = %d"%(len(traceback)-1)



	print "=================================<< END  >>======================================"	


