#!/usr/bin/python
# Created by Joao A. Jesus Jr. <joao29a@gmail.com>
#            Joao M. Velasques Faria
import sys
import math
import AStar

class NumberPuzzle(AStar.AStar):
    def __init__(self,heuristic):
        self.heuristic = heuristic

    def distBetween(self,current,neighbor):
        coord = []
        for i in range(len(current)):
            for j in range(len(current[i])):
                if current[i][j] == 0 or neighbor[i][j] == 0:
                    coord.append([i,j])
                if len(coord) == 2:
                    firstPosition = pow(coord[0][0] - coord[1][0],2)
                    secondPosition = pow(coord[0][1] - coord[1][1],2)
                    return math.sqrt(firstPosition + secondPosition)
        return 0

    def firstHeuristic(self,start,goal,i,j):
        if start[i][j] != goal[i][j]:
            self.cost += 1

    def secondHeuristic(self,start,goal,i,j):
        if j + 1 < len(start[i]):
            if start[i][j] != start[i][j+1] - 1:
                self.cost += 1
        elif i + 1 < len(start):
            if start[i][j] != start[i+1][0] - 1:
                self.cost += 1

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
            self.cost += math.sqrt(pow(correctI - i,2) + pow(correctJ - j,2))

    def heuristicEstimate(self,start,goal):
        self.cost = 0
        for i in range(len(start)):
            for j in range(len(start[i])):
                if self.heuristic & 0b1:
                    self.firstHeuristic(start,goal,i,j)
                if self.heuristic & 0b10:
                    self.secondHeuristic(start,goal,i,j)
                if self.heuristic & 0b100:
                    self.thirdHeuristic(start,goal,i,j)
        return self.cost

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
        for i in path:
            for j in i:
                for k in j:
                    print "%2d" % k,
                print
            print
        print "%d Movements" % (len(path) - 1)

if __name__ == "__main__":
    finalState = ((1,2,3,4),(5,6,7,8),(9,10,11,12),(13,14,15,0))
    
    examples = {
            1: ((1,6,2,3),(5,10,7,4),(9,14,11,8),(13,0,15,12)),
            2: ((2,0,3,4),(1,6,7,8),(5,9,10,11),(13,14,15,12)),
            3: ((2,6,8,3),(1,14,9,11),(7,12,13,0),(5,15,4,10)),
            4: ((1,6,2,3),(5,10,7,0),(4,9,14,11),(8,13,15,12)),
            5: ((1,6,2,3),(5,10,0,7),(4,9,14,11),(8,13,15,12)),
            6: ((1,6,2,3),(5,0,10,7),(4,9,14,11),(8,13,15,12)),
            7: ((1,6,2,3),(0,5,10,7),(4,9,14,11),(8,13,15,12)),
            }

    if len(sys.argv) > 2:
        ex = int(sys.argv[1])
        heuristic = None
        
        try:
            heuristic = int(sys.argv[2],2)
        except:
            print "Insert a binary number for the second arg."
            sys.exit(1)
        
        if ex in examples:
            try:
                puzzle = NumberPuzzle(heuristic)
                path = puzzle.aStar(examples[ex],finalState)
                puzzle.printPath(path)
            except:
                print "Program interrupted."
                sys.exit(1)
        else:
            print "Invalid arg."
    
    else:
        print "Insert two args."
        for keys in examples:
            print keys,
        print "\nAnd a binary number."
