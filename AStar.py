#!/usr/bin/python
# Created by Joao A. Jesus Jr. <joao29a@gmail.com>
#            Joao M. Velasques Faria

from collections import deque
import heapq

#This class is used to maintain a heap
class Node:
    def __init__(self,node,value):
        self.node = node
        self.value = value

    #Operator overloading. Maintaining a min heap
    def __lt__(self,other):
        return self.value < other.value

class AStar:
    def distBetween(self,current,neighbor):
        pass

    def heuristicEstimate(self,start,goal):
        pass

    def neighborNodes(self,current):
        pass

    def reconstructPath(self,cameFrom,goal,closedSetSize,openSetSize):
        path = deque()
        node = goal
        path.appendleft(node)
        while node in cameFrom:
            node = cameFrom[node]
            path.appendleft(node)
        path.append(closedSetSize)
        path.append(openSetSize)
        return path

    #Return the root node (min value) and maintain the heap O(log n)
    def getLowest(self,heapQueue):
        return heapq.heappop(heapQueue).node

    def aStar(self,start,goal):
        cameFrom = {}
        openSet = {start}
        closedSet = set()
        gScore = {}
        fScore = {}
        gScore[start] = 0
        fScore[start] = gScore[start] + self.heuristicEstimate(start,goal)
        heapQueue = [Node(start,fScore[start])]
        while len(openSet) != 0:
            current = self.getLowest(heapQueue)
            if current == goal:
                return self.reconstructPath(cameFrom,goal,len(closedSet),len(openSet))
            openSet.remove(current)
            closedSet.add(current)
            for neighbor in self.neighborNodes(current):
                tentative_gScore = gScore[current] + self.distBetween(current,neighbor)
                if neighbor in closedSet and tentative_gScore >= gScore[neighbor]:
                    continue
                if neighbor not in closedSet or tentative_gScore < gScore[neighbor]:
                    cameFrom[neighbor] = current
                    gScore[neighbor] = tentative_gScore
                    fScore[neighbor] = gScore[neighbor] + self.heuristicEstimate(neighbor,goal)
                    if neighbor not in openSet:
                        heapq.heappush(heapQueue,Node(neighbor,fScore[neighbor]))
                        openSet.add(neighbor)
        return 0
