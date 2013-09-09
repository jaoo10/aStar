from collections import deque

def dist_between(current,neighbor):
    return 0

def heuristic_cost_estimate(start,goal):
    return 0

def reconstruct_path(cameFrom, goal):
    path = deque()
    path.appendleft(goal)
    node = goal
    while node in cameFrom:
        node = cameFrom[node]
        path.appendleft(node)
    return path

def neighbor_nodes(current):
    return {"middle", "end"}

def getLowest(openSet, fScore):
    lowest = float("inf")
    lowestNode = None
    for node in openSet:
        if fScore[node] < lowest:
            lowest = fScore[node]
            lowestNode = node
    return lowestNode

def aStar(start,goal):
    cameFrom = {}
    openSet = set([start])
    closedSet = set()
    gScore = {}
    fScore = {}
    gScore[start] = 0
    fScore[start] = gScore[start] + heuristic_cost_estimate(start,goal)
    while len(openSet) != 0:
        current = getLowest(openSet,fScore)
        if current == goal:
            return reconstruct_path(cameFrom,goal)
        openSet.remove(current)
        closedSet.add(current)
        for neighbor in neighbor_nodes(current):
            tentative_gScore = gScore[current] + dist_between(current,neighbor)
            if neighbor in closedSet and tentative_gScore >= gScore[neighbor]:
                continue
            if neighbor not in closedSet or tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + heuristic_cost_estimate(neighbor,goal)
                if neighbor not in openSet:
                    openSet.add(neighbor)
    return 0

if __name__ == "__main__":
    path = aStar("begin","end")
    if path == 0:
        print "Failed"
    else:
        for node in path:
            print(node),
