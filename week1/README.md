Week 1
====================
--------
###Week 1 Documents:
The topics for this week were fairly light.  Topics include: an introduction to planning, and
an informal overview of the planning problem, as well as a brief overview of planning's relation
to search, as well as how to define search problems via the use of tree structures (general graph
structures are discussed in less detail).


--------
###Week 1 Problems:

* Missionaries and Cannibals Search Problem

On one bank of a river are three missionaries (black triangles) and three cannibals (red circles). 
There is one boat available that can hold up to two people and that they would like to use to cross
the river. If the cannibals ever outnumber the missionaries on either of the river’s banks, the
missionaries will get eaten.  For the boat to move, it must always have at least one person inside.

How can the boat be used to safely carry all the missionaries and cannibals across the river?

Try to implement the general search algorithm just described. You can use LIFO and FIFO as queuing
strategies to determine the order in which nodes are explored. These two strategies are known as
depth-first and breadth-first search respectively. Be careful, depth-first search may descend down
infinite branches, so best implement a depth cut-off. Then, extend your implementation with a hash
table that stores all the nodes found so far. Print out a trace of the states the algorithm finds
(in the order they are discovered) and see how much of the search space each algorithm explores.