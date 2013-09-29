#!/usr/bin/python
# Created by Joao A. Jesus Jr. <joao29a@gmail.com>
#            Joao M. Velasques Faria
import sys
import math
import AStar
import time

class NumberPuzzle(AStar.AStar):
    #Choose which heuristic to use, weight1 is the weight of the 1st heuristic
    #and so on.
    def __init__(self,weight1,weight2,weight3):
        self.weight1 = weight1
        self.weight2 = weight2
        self.weight3 = weight3

    #Manhattan distance of the empty square
    def distBetween(self,current,neighbor):
        coord = []
        for i in range(len(current)):
            for j in range(len(current[i])):
                if current[i][j] == 0 or neighbor[i][j] == 0:
                    coord.append([i,j])
                if len(coord) == 2:
                    firstPosition = abs(coord[0][0] - coord[1][0])
                    secondPosition = abs(coord[0][1] - coord[1][1])
                    return firstPosition + secondPosition
        return 0

    def firstHeuristic(self,start,goal,i,j):
        if start[i][j] != goal[i][j]:
            self.cost1 += 1

    def secondHeuristic(self,start,goal,i,j):
        if j + 1 < len(start[i]):
            if start[i][j] != start[i][j+1] - 1:
                self.cost2 += 1
        elif i + 1 < len(start):
            if start[i][j] != start[i+1][0] - 1:
                self.cost2 += 1

    #Manhattan distance
    def thirdHeuristic(self,start,goal,i,j):
        if start[i][j] != goal[i][j]:
            correctI = None
            correctJ = None
            if start[i][j] == 0:
                correctI = len(start) - 1
                correctJ = len(start[i]) - 1
            else:
                correctI = (start[i][j] - 1) / len(start)
                correctJ = (start[i][j] - 1) % len(start[i])
            self.cost3 += abs(correctI - i) + abs(correctJ - j)

    def heuristicEstimate(self,start,goal):
        self.cost1 = 0
        self.cost2 = 0
        self.cost3 = 0
        for i in range(len(start)):
            for j in range(len(start[i])):
                    self.firstHeuristic(start,goal,i,j)
                    self.secondHeuristic(start,goal,i,j)
                    self.thirdHeuristic(start,goal,i,j)
        self.cost1 *= self.weight1
        self.cost2 *= self.weight2
        self.cost3 *= self.weight3
        return self.cost1 + self.cost2 + self.cost3

    def neighborNodes(self,current):
        for i in range(len(current)):
            for j in range(len(current[i])):
                if current[i][j] == 0:
                    nodes = []
                    if i-1 >= 0:
                        nodes.append(self.makeMove(current,i-1,j,i,j))
                    if i+1 < len(current):
                        nodes.append(self.makeMove(current,i+1,j,i,j))
                    if j-1 >= 0:
                        nodes.append(self.makeMove(current,i,j-1,i,j))
                    if j+1 < len(current[i]):
                        nodes.append(self.makeMove(current,i,j+1,i,j))
                    return nodes
        return []

    def makeMove(self,current,i,j,x,y):
        lst = map(list,current)
        temp = lst[x][y]
        lst[x][y] = lst[i][j]
        lst[i][j] = temp
        return tuple(map(tuple,lst))

    def printPath(self,path):
        openSetSize = path.pop()
        closedSetSize = path.pop()
        for i in path:
            for j in i:
                for k in j:
                    print "%2d" % k,
                print
            print
        print("%s Movements" % "{:,}".format((len(path) - 1)))
        print("OpenSet size: %s" % "{:,}".format(openSetSize))
        print("ClosedSet size: %s" % "{:,}".format(closedSetSize))
        print("Total nodes: %s" % "{:,}".format(openSetSize + closedSetSize))

def getPuzzle(filename):
    f = open(filename)
    puzzle = []
    for line in f:
        puzzle.append(tuple(map(int,line.split())))
    f.close()
    return tuple(puzzle)

if __name__ == "__main__":
    argc = 5
    if len(sys.argv) > argc:
        try:
            example = getPuzzle(sys.argv[1])
            finalState = getPuzzle(sys.argv[2])
            weight1 = float(sys.argv[3])
            weight2 = float(sys.argv[4])
            weight3 = float(sys.argv[5])
            puzzle = NumberPuzzle(weight1,weight2,weight3)
            timeInit = time.time()
            path = puzzle.aStar(example,finalState)
            timeEnd = time.time() - timeInit
            puzzle.printPath(path)
            print("Time: %f seconds" % timeEnd)
        
        except BaseException as error:
            print(error)
            sys.exit(1)
    
    else:
        print "Insert %d args." % argc
