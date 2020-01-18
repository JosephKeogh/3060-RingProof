import random
import statistics
import matplotlib.pyplot as plt
import sys


def notVisitedCount(arr):
    """

    :param arr: array containing info about if the node (with the number being the index was visited
    :return: the count of the nodes that have not been visited
    """

    notVisited = 0

    for a in arr:
        if a == 'no':
            notVisited += 1

    return notVisited

def findNotVisited(arr):
    '''

    :param arr: list of nodes that only has one node that has not been visited
    :return: the index 'name' of the node that has not been visited yet
    '''

    length = arr.__len__()

    for i in range(0, length):

        if arr[i] == 'no':
            return i

def simulation(nodeCount):
    '''

    :param nodes: the number of nodes you want
    :return: the name of the last node visited
    '''

    # a list of whether the nodes have been visited, the index is the name
    nodesVisited = []
    for i in range(0, nodeCount):
        nodesVisited.append('no')

    # count of nodes not visited
    notVisited = notVisitedCount(nodesVisited)

    # the highest value of a node
    maxNode = nodeCount - 1

    # the node we are currently on
    currentNode = 0

    # perform the simulation while there is more than one node left
    while notVisited > 1:

        # update the new node to be visited
        nodesVisited[currentNode] = 'yes'

        # probability
        
        val = random.random()

        # equal probability of going left or right, plus or minus one
        if val < 0.5:

            # update the current node
            currentNode += 1

            # adjust for the nodes being in a circle
            if currentNode > maxNode:
                currentNode = 0

        else:

            # update the current node
            currentNode -= 1

            # adjust for the nodes being in a circle
            if currentNode < 0:
                currentNode = maxNode

        # update the nodes not visited count
        notVisited = notVisitedCount(nodesVisited)

    return currentNode

def manySimulations(runs, nodes, t):

    # record of nodes visited last
    visitedLast = []

    # run the simulation many times:
    for i in range(0, runs):

        # keep track of progress
        percent = i * 100 / runs
        if (percent % 25 == 0) & (t == True):
            print(percent)

        simResult = simulation(nodes)
        visitedLast.append(simResult)

    return visitedLast

def findErrors(simResults, nodeCount):
    '''

    :param simResults: the list with the last nodes seen
    :param nodeCount: the count of the nodes
    :return:
    '''

    # will have the name of the last node seen for each run in the simulation
    seen = {}

    # the number of simulations
    simCount = simResults.__len__()

    for a in simResults:
        if a in seen:
            seen[a] += 1
        else:
            seen[a] = 1

    # change the count for each node to the proportion it was seen relative to the other nodes
    for a in seen:

        # the new value will be (the amount this node was seen) / ( the total number of simulations )
        seen[a] = seen[a] / simCount

    # the expected proportion for each node
    # we expect each node to be seen 1/totalNode times
    # this is if the assumption is correct
    expectedProp = 1 / nodeCount

    # all the errors
    errors = []
    for i in seen:

        # the proportion that this node was visited last
        observedProp = seen[i]

        # the error in the observation vs what we expected
        error = abs(observedProp - expectedProp)

        # add the error to a holder
        errors.append(error)

    return errors

def main():

    # the runs of the simulation to do
    runs =          int(sys.argv[1])
    minNodeCount =  int(sys.argv[2])
    maxNodeCount =  int(sys.argv[3])
    step =          int(sys.argv[4])

    # keep track of the averages through multiple simulations with multiple node counts
    averageErrors = []

    # nodes
    nodeValues = []

    print("Node Count Values:")
    # run process for multiple counts of nodes
    for nodes in range(minNodeCount, maxNodeCount, step):

        print(str(nodes) + " Nodes")

        # keep track of the node values
        nodeValues.append(nodes)

        # run the simulation with the appropriate number of runs and nodes
        sims = manySimulations(runs, nodes, False)

        # collect the error terms
        errors = findErrors(sims, nodes)

        # the average of the error terms
        average = statistics.mean(errors)

        # add the average error term to the list of average errors
        averageErrors.append(average)

    # the average of the average errors
    doubleAverage = statistics.mean(averageErrors)
    print("Average Error:")
    print(doubleAverage)

    # plot the average errors
    # create x values
    x = nodeValues
    y = averageErrors
    plt.plot(x, y, label = "Average Time per Node Amount")

    x = nodeValues
    y = []
    for i in x:
        y.append(doubleAverage)

    plt.plot(x, y, label = "Overall Average")

main()
plt.show()
print('finished')

# end of file
