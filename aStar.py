def dist_between(current,neighbor):
    return 0

def heuristic_cost_estimate(start,goal):
    return 0

def reconstruct_path(cameFrom, currentNode):
    return 0

def neighbor_nodes(current):
    return {1: 2, 3: 4}

def aStar(start,goal):
    closedSet = {}
    openSet = {start}
    cameFrom = {}
    gScore = {}
    gScore[start] = 0
    fScore = {}
    fScore[start] = gScore[start]+heuristic_cost_estimate(start,goal)
    while len(openSet) != 0:
        #current = 0 the node in openSet having the lowest fScore[] value
        current = 0
        if current == goal:
            return reconstruct_path(cameFrom,goal)
        #remove current from openSet
        #add current to closedSet
        for neighbor in neighbor_nodes(current):
            tentative_gScore = gScore[current] + dist_between(current,neighbor)
            if neighbor in closedSet and tentative_gScore >= gScore[neighbor]:
                continue
            if neighbor not in closedSet or tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + heuristic_cost_estimate(neighbor,goal)
                if neighbor not in openSet:
                    test = 0
                    #add neighbor to openSet
    return 1

if __name__ == "__main__":
    print aStar(0,1)
