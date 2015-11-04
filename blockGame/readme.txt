StepsTo Run:
Execute main.py by command
Make main.py executable by:
chmod +x main.py
.\main.py  no_of_stacks no_of_blocks arg3 --g -–p --d

no_of_stacks  : No. of stacks (default value: 3)
no_of_blocks : No of Blocks( default value: 5)
arg3	           :  Type of Heuristic (“custom” or “default”) by default it will run for both and when it 			  executes for both it generates report also as “report.html”  having statistics and path to 			  files having path to goal state.
--g (optional) : Use Greedy approach instead of ASTAR, default value is false.
--p (optional): Deletes extra priority queue elements when it crosses certain limit, default value is false.
--d (optional) : To see traces, default is false

