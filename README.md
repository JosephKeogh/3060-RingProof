# 3060-RingProof

## This is a simulation of a problem where nodes are arranged in a circle.  You start at node 0, and each turn have an equal probability of going left or right (+ or - one node).  Which node are you most likely to visit last.  This sim hopes to show that there is an equal likelyhood of visiting any one node last.

## To run the code, just enter "python simulation-3060.py a b c d"  where a,b,c,d are integer values.

### a = runs of the simulation per node count
### b = the min number of nodes you want in the ring
### c = the max number of nodes you want in the ring
### d = the step you want the program to proceed ( if 1, the simulation will run every node count between your min and max nodes.  If 2, the program will run every other node count between your min and max nodes.

## I suggest running a = 100, b = 3, c = 100, and d = 1 to start.

## The output is a graph that shows the errors with respect to the assumption.  This means if there are 10 nodes, we expect each node to be visited last 10% of the time.  If the simulation finds a node that was visited 9% of the time, the error displayed will be 1%.
