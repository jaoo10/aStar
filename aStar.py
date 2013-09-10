from collections import deque

def dist_between(current,neighbor):
    coord = []
    for i in range(len(current)):
        for j in range(len(current[i])):
            if current[i][j] == 0 or neighbor[i][j] == 0:
                coord.append([i,j])
            if len(coord) == 2:
                firstPosition = coord[0][0] * len(current) + coord[0][1]
                secondPosition = coord[1][0] * len(current) + coord[1][1]
                return abs(firstPosition - secondPosition)
    return 0


def heuristic_cost_estimate(start,goal):
    cost = 0
    for i in range(len(start)):
        for j in range(len(start[i])):
            if start[i][j] != goal[i][j]:
                cost += 1
    return cost

def reconstruct_path(cameFrom, goal):
    path = deque(goal)
    node = goal
    while node in cameFrom:
        node = cameFrom[node]
        path.appendleft(node)
    return path

def makeMove(current,i,j,x,y):
    lst = map(list,current)
    temp = lst[x][y]
    lst[x][y] = lst[i][j]
    lst[i][j] = temp
    return tuple(map(tuple,lst))

def neighbor_nodes(current):
    for i in range(len(current)):
        for j in range(len(current[i])):
            if current[i][j] == 0:
                nodes = []
                if i-1 >= 0:
                    nodes.append(makeMove(current,i-1,j,i,j))
                if i+1 < len(current):
                    nodes.append(makeMove(current,i+1,j,i,j))
                if j-1 >= 0:
                    nodes.append(makeMove(current,i,j-1,i,j))
                if j+1 < len(current[i]):
                    nodes.append(makeMove(current,i,j+1,i,j))
                return nodes
    return []

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
    initialState = (( 0, 15,  1,  2),
                    ( 4,  3, 14, 13),
                    ( 5,  7, 11, 12),
                    (10,  8,  6,  9))

    finalState = (( 1,  2,  3,  4),
                  ( 5,  6,  7,  8),
                  ( 9, 10, 11, 12),
                  (13, 14, 15,  0))

    path = aStar(initialState,finalState)
    print "%d Movimentos" % len(path)-1
